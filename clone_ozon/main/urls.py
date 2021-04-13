from django.urls import path, include
from .views import index,about,ProductList, ProductDetail
from django.contrib.flatpages import views
from .views import update_profile


urlpatterns = [
    path('', index),
    path('about/', about),
    path('goods/', ProductList.as_view()),
    path("goods/<int:pk>/", ProductDetail.as_view()),
    path('accounts/profile/', update_profile, name='profile'),
]
