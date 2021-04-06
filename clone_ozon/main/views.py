from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Seller


def index(request):
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


class ProductList(ListView):
    model = Product
    template_name='main/product_list.html'
    

class ProductDetail(DetailView):
    template_name='main/product_details.html'
    model = Product
    slug_url_kwarg='pk'
    context_object_name='product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('--------------------')
        print(context['product'])
        print('--------------------')
        # context["name"] = self.kwargs['name'] 
        return context
    
