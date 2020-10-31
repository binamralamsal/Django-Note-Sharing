from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import models
import datetime as dt


def home(request):
    return render(request, 'paste/home.html')


def get_text(request, pk):
    password = request.GET.get('p')
    text = get_object_or_404(models.TextFile, pk=pk)
    private = False
    if text.security == 'PRIVATE':
        if text.author == request.user:
            private = False
        else:
            private = True
    if text.expiration_date and text.expiration_date < dt.date.today():
        expired = True
    else:
        expired = False
    if text.key and text.key != password:
        password_given = False
    else:
        password_given = True
    context = {
        'paste': text,
        'password': password_given,
        'expired': expired,
        'private': private
    }
    return render(request, 'paste/text.html', context)


@login_required(login_url='login')
def add_text_form(request):
    return render(request, 'paste/add-text.html')


@login_required(login_url='login')
def add_text(request):
    if request.method == "POST":
        text = request.POST['text']
        paste = models.TextFile(author=request.user, text=text)
        paste.save()
        return redirect('my_paste')
    else:
        return redirect('add')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'paste/dashboard/base.html')


@login_required(login_url='login')
def my_pastes(request):
    paste = models.TextFile.objects.filter(author=request.user)
    return render(request, 'paste/my-paste.html', {'paste': paste})