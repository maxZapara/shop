from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))
    username=forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Enter your username'}))
    password1=forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))
    password2=forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'Confirm your password'}))
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('User with this email already exists')
        return email


class LoginForm(AuthenticationForm):
    username=forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Enter your username or email'}))
    password=forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))
    class Meta:
        model=User
        fields=['username', 'password']