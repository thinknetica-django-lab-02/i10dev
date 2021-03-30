from django.shortcuts import render


def index(request):
    return render(request, 'main/main.html', {
        'title': 'Main'
    })


def about(request):
    return render(request, 'main/about.html', {
        'title': 'About'
    })
