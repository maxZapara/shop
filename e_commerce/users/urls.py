from django.contrib import admin
from django.urls import path
from .views import auth_login, auth_signup, google_callback

urlpatterns = [
    path('auth/login',auth_login, name='login'), 
    path('auth/signup',auth_signup, name='signup'),   
    path("google/login/callback",google_callback, name="callback")


]