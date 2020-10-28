from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import models


def home(request):
    return render(request, 'paste/home.html')


def get_text(request, pk):
    text = get_object_or_404(models.TextFile, pk=pk)
    return render(request, 'paste/text.html', {'paste': text})


def add_text_form(request):
    return render(request, 'paste/add-text.html')


def add_text(request):
    if request.method == "POST":
        text = request.POST['text']
        paste = models.TextFile(author=request.user, text=text)
        paste.save()
        return redirect('/')
    else:
        return redirect('add')


def dashboard(request):
    return render(request, 'paste/dashboard/index.html')