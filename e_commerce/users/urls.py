from django.contrib import admin
from django.urls import path
from .views import auth_login, auth_signup

urlpatterns = [
    path('auth/login',auth_login, name='login'), 
    path('auth/signup',auth_signup, name='signup'),   


]