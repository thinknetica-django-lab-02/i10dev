from django.urls import path, include
from .views import index,about,ProductList, ProductDetail,UpdateView
from django.contrib.flatpages import views


urlpatterns = [
    path('', index),
    path('about/', about),
    path('goods/', ProductList.as_view()),
    path("goods/<int:pk>/", ProductDetail.as_view()),
    path('accounts/profile/', UpdateView.as_view(), name='profile')
]
