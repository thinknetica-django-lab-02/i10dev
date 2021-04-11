from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Seller, Tag
from django.views.generic.edit import FormView
from .forms import ProfileForm

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
    paginate_by = 3
    template_name = 'main/product_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        tag = self.request.GET.get('tag')
        context['tag'] = tag
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        tag = self.request.GET.get('tag')
        if tag:
            return queryset.filter(tag__name=tag)
        return queryset


class ProductDetail(DetailView):
    template_name = 'main/product_details.html'
    model = Product
    slug_url_kwarg = 'pk'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        return context

class UpdateView(FormView):
    template_name = 'user.html'


    def get(self, request, *args, **kwargs):
        return render(request, 'main/user.html', {'form': ProfileForm()})

    