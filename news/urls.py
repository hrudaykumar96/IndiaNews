from django.urls import path
from .views import home, full_latest_news_view, full_trending_news_view, full_headlines_view, full_articles_view, get_news_bycategory, create_category, create_latest_news, create_headline, create_article, create_trending_news, news_management, category_management, delete_news, update_category, update_news, delete_category, profile

urlpatterns = [
    path('',home, name='home'),
    path('news/latestnews/<slug:slug>/',full_latest_news_view, name='Latest_News'),
    path('news/trendingnews/<slug:slug>/',full_trending_news_view, name='Trending_News'),
    path('news/headlines/<slug:slug>/',full_headlines_view, name='Headlines'),
    path('news/article/<slug:slug>/',full_articles_view, name='Articles'),
    path('news/<slug:slug>/',get_news_bycategory, name='get_news_bycategory'),
    path('add/category/',create_category, name='create_category'),
    path('add/latestnews/',create_latest_news, name='create_latest_news'),
    path('add/headline/',create_headline, name='create_headline'),
    path('add/article/',create_article, name='create_article'),
    path('add/trendingnews/',create_trending_news, name='create_trending_news'),
    path('news/',news_management, name='news_management'),
    path('category/',category_management, name='category_management'),
    path('deletenews/<slug:slug>/',delete_news, name='delete_news'),
    path('update/category/<slug:slug>/',update_category, name='update_category'),
    path('update/news/<slug:slug>/',update_news, name='update_news'),
    path('delete/category/<slug:slug>/',delete_category, name='delete_category'),
    path('profile/<str:user_id>/',profile, name='profile'),
]