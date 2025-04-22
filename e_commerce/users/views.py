from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.
def auth_login(request):
    form=LoginForm()
    if request.method == 'POST':
        form=LoginForm(request, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            messages.success(request, f'Welcome {user.username}')
            login(request, user)
            print(user)
            return redirect('home')
        else:
            for field,errors in form.errors.items():
                for e in errors:
                    messages.error(request,f"{field.capitalize()} : {e}")
                    print(e)
    
    return render(request, 'users/login.html', {'login_form': form})

def auth_signup(request):
    form=RegistrationForm()
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request, 'Registration successful. Confirm your email please')
            print(user)
            return redirect('login')
        else:
            for field,errors in form.errors.items():
                for e in errors:
                    messages.error(request,f"{field.capitalize()} : {e}")
                    print(e)
    
    return render(request, 'users/registration.html', {'registration_form': form})


def google_callback(request):
    print("google_callback")
    return redirect("home")