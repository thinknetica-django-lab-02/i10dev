from django.shortcuts import render
from .models import Category

def index(request):
    return render(request, 'main/main.html', {
        'title': 'Main'
    })


def about(request):
    return render(request, 'main/about.html', {
        'title': 'About'
    })
