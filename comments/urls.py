from .views import post_comments, post_reply, delete_comment, delete_reply, edit_comments, update_reply
from django.urls import path

urlpatterns = [
    path('comments/<slug:slug>/',post_comments, name='post_comments'),
    path('comments/edit/<int:id>/<slug:slug>/',edit_comments, name='edit_comments'),
    path('reply/<int:id>/<slug:slug>/',post_reply, name='post_reply'),
    path('comments/delete/<int:id>/',delete_comment, name='delete_comment'),
    path('reply/delete/<int:id>/',delete_reply, name='delete_reply'),
    path('reply/edit/<int:id>/<slug:slug>/',update_reply, name='update_reply'),
]