from django.urls import path, include
from .views import index, about
from django.contrib.flatpages import views

urlpatterns = [
    path('', index),
]
