from django.db import models
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

# Create your models here.

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        try:
            print("back: ", username, password)
            user=User.objects.get(email=username) if "@" in username else User.objects.get(username=username)
            print("user: ", user)
            if user.check_password(password):
                return user
        except:
            return None
