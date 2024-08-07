from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, name, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=500)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    slug=models.SlugField(max_length=1000,unique=True, blank=True)
    image = models.ImageField(upload_to='profile/', blank=True, null=False)
    description=models.TextField(blank=True, null=False)
    facebook = models.CharField(max_length=500, blank=True, null=False)
    linkedin = models.CharField(max_length=500, blank=True, null=False)
    instagram = models.CharField(max_length=500, blank=True, null=False)
    twitter = models.CharField(max_length=500, blank=True, null=False)
    skype = models.CharField(max_length=500, blank=True, null=False)
    user_id = models.CharField(max_length=500, unique=True, blank=True, null=True)

    USER='user'
    ADMIN='admin'
    EDITOR='editor'
    
    choices=[
        (USER,'user'),(ADMIN, 'admin'),(EDITOR,'editor')
    ]
    
    role = models.CharField(max_length=100, choices=choices, default=USER)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.email)
        if not self.user_id:
            self.user_id = self.email.split('@')[0]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

@receiver(post_delete, sender=CustomUser)
def delete_latest_news_image(sender, instance, **kwargs):
    if instance.image:
        storage, path = instance.image.storage, instance.image.path
        if os.path.isfile(path):
            storage.delete(path)