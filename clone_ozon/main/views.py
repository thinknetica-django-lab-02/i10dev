from django.shortcuts import render
from .queries import test


def index(request):
    test()
    return render(request, 'main/main.html', {
        'title': 'Main'
    })


def about(request):
    return render(request, 'main/about.html', {
        'title': 'About'
    })
