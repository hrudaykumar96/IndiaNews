from django.contrib import admin
from .models import Category, Latest_News, Articles, Trending_News, Headlines
# Register your models here.

admin.site.register(Category)
admin.site.register(Latest_News)
admin.site.register(Headlines)
admin.site.register(Articles)
admin.site.register(Trending_News)