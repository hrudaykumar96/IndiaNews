from django.urls import path
from .views import loginuser, signupuser, signout, change_password, reset_password, create_editor, user_management, delete_users, update_user, update_profile

urlpatterns = [
    path('login/', loginuser, name="loginuser"),
    path('signup/', signupuser, name="signupuser"),
    path('logout/', signout, name="signout"),
    path('change-password/', change_password, name="change_password"),
    path('reset-password/', reset_password, name="reset_password"),
    path('create-admin/', create_editor, name="create_admin"),
    path('users/', user_management, name="user_management"),
    path('delete/<slug:slug>/', delete_users, name="delete_users"),
    path('update/<slug:slug>/', update_user, name="update_user"),
    path('update/profile/<str:user_id>/', update_profile, name="update_profile"),
]