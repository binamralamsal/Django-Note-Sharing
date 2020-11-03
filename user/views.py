from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth, messages

from paste.models import TextFile


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'auth/login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'auth/register.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are logged in successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "Either email or password is incorrect")
            return redirect('login')
    else:
        messages.error(request, "Internal Error Occurred!")
        return redirect('home')


def register_user(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']

        # To check if user is registered already or not
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email with that user already exists!")
            return redirect('register')
        if password == password_repeat:
            if len(password) >= 8:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=email, password=password)
                user.save()
                auth.login(request, user)
                messages.success(request, "Your new user is created successfully!")
                return redirect('dashboard')
            else:
                messages.error(request, "Sorry but minimum of 8 letters are required for password.")
                return redirect('register')
        else:
            messages.error(request, "Password does not match")
        return redirect('register')
    else:
        messages.error(request, "Internal Error Occurred!")
        return redirect('home')


def profile(request):
    paste = TextFile.objects.count()
    return render(request, 'auth/profile.html', {'paste': paste})


def edit_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.save()
        messages.success(request, "Profile Update successfully.")
        return redirect('profile')
    else:
        messages.error(request, "Internal error occurred")
        return redirect('profile')