from django.contrib import admin
from django.urls import re_path, path
from . import views
from rest_framework_jwt.views import  (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

urlpatterns = [
    path('login/', obtain_jwt_token, name='login_token'),
    path('refresh/', refresh_jwt_token, name='refresh_token'),
    path('verify/', verify_jwt_token, name='verify_token'),
    path('adduser/', views.UserManager.add_user, name='create user'),
    path('change_password/', views.UserManager.update_password, name='Change Password'),
    path('delete_user/<int:user_id>/', views.UserManager.delete_user, name='Delete User'),
]
