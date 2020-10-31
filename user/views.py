from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth


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
    return redirect('home')


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        return redirect('login')


def register_user(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']
        if password == password_repeat:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=email, password=password)
            user.save()
            auth.login(request, user)
            return redirect('dashboard')
        return redirect('register')