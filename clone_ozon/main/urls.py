from django.urls import path, include
from .views import index,about,ProductList, ProductDetail
from django.contrib.flatpages import views


urlpatterns = [
    path('', index),
    path('about/', about),
    path('goods/', ProductList.as_view()),
    path("goods/<int:pk>/", ProductDetail.as_view())
]
