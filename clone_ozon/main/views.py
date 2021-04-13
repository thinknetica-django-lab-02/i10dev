from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView
from .models import Product, Seller, Tag, Profile
from django.views.generic.edit import FormView
from .forms import Profile

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from .forms import UserForm

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


# class ProfileView(FormView):
#     template_name = 'user.html'
#     formset_class = ProfileFormSet
#     fields = ['first_name', 'last_name', 'email']
    
#     def get(self, request, *args, **kwargs):
#         return render(request, 'main/user.html', { 'form': Profile() } )
    
#     def get_object(self, queryset=None):
#         return self.request.user
    
@login_required
@transaction.atomic
def update_profile(request):
    User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
    ProfileFormset = inlineformset_factory(User, Profile, fields='__all__', can_delete=False)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        formset = ProfileFormset(request.POST, instance=request.user)
        
    else:
        user_form = UserForm(instance=request.user)
        formset = ProfileFormset(instance=request.user.profile)
    return render(request, 'main/user.html', locals())