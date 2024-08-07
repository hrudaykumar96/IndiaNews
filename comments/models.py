from django.db import models
from users.models import CustomUser
from news.models import Articles, Latest_News, Headlines, Trending_News
from django.utils import timezone

# Create your models here.

class Comments(models.Model):
    text=models.TextField(blank=True, null=True)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    time=models.DateTimeField(default=timezone.now)
    articles=models.ForeignKey(Articles, on_delete=models.SET_NULL, null=True, blank=True)
    latest_news=models.ForeignKey(Latest_News, on_delete=models.SET_NULL, null=True, blank=True)
    headlines=models.ForeignKey(Headlines, on_delete=models.SET_NULL, null=True, blank=True)
    trending_news=models.ForeignKey(Trending_News, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.text
    

class Reply(models.Model):
    text=models.TextField(blank=True, null=True)
    comment=models.ForeignKey(Comments, on_delete=models.CASCADE)
    time=models.DateTimeField(default=timezone.now)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    articles=models.ForeignKey(Articles, on_delete=models.SET_NULL, null=True, blank=True)
    latest_news=models.ForeignKey(Latest_News, on_delete=models.SET_NULL, null=True, blank=True)
    headlines=models.ForeignKey(Headlines, on_delete=models.SET_NULL, null=True, blank=True)
    trending_news=models.ForeignKey(Trending_News, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.text