from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from tinymce.models import HTMLField
from django.utils.html import strip_tags
from users.models import CustomUser
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

class Category(models.Model):
    name=models.CharField(max_length=1000)
    created=models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=1000, unique=True, blank=True)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Latest_News(models.Model):
    title=models.CharField(max_length=1000)
    publish_date=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='images/')
    description=HTMLField()
    content=models.TextField(blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=1000, unique=True, blank=True)
    is_acknowledge=models.BooleanField(default=False)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        self.content = strip_tags(self.description)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title   
    
@receiver(post_delete, sender=Latest_News)
def delete_latest_news_image(sender, instance, **kwargs):
    if instance.image:
        storage, path = instance.image.storage, instance.image.path
        if os.path.isfile(path):
            storage.delete(path)
    

class Trending_News(models.Model):
    title=models.CharField(max_length=1000)
    publish_date=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='images/')
    description=HTMLField()
    content=models.TextField(blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=1000, unique=True, blank=True)
    is_acknowledge=models.BooleanField(default=False)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        self.content = strip_tags(self.description)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
    
@receiver(post_delete, sender=Trending_News)
def delete_latest_news_image(sender, instance, **kwargs):
    if instance.image:
        storage, path = instance.image.storage, instance.image.path
        if os.path.isfile(path):
            storage.delete(path)
    
class Headlines(models.Model):
    title=models.CharField(max_length=1000)
    publish_date=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='images/')
    description=HTMLField()
    content=models.TextField(blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=1000, unique=True, blank=True)
    is_acknowledge=models.BooleanField(default=False)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        self.content = strip_tags(self.description)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

@receiver(post_delete, sender=Headlines)
def delete_latest_news_image(sender, instance, **kwargs):
    if instance.image:
        storage, path = instance.image.storage, instance.image.path
        if os.path.isfile(path):
            storage.delete(path)
    

class Articles(models.Model):
    title=models.CharField(max_length=1000)
    publish_date=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='images/')
    description=HTMLField()
    content=models.TextField(blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=1000, unique=True, blank=True)
    is_acknowledge=models.BooleanField(default=False)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        self.content = strip_tags(self.description)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
    
@receiver(post_delete, sender=Articles)
def delete_latest_news_image(sender, instance, **kwargs):
    if instance.image:
        storage, path = instance.image.storage, instance.image.path
        if os.path.isfile(path):
            storage.delete(path)