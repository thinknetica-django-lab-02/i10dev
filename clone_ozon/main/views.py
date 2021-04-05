from django.shortcuts import render
# from .queries import test


def index(request):
    # test()
    return render(request, 'main/main.html', {
        'title': 'Main',
        'user': request.user,
        'turn_on_block': True
    })


def about(request):
    return render(request, 'flatpages/default.html', {
        'title': 'About',
        'turn_on_block': False
    })
