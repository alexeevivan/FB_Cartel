from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect, request
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView, View, ListView, CreateView
from django.contrib.auth import logout
from .models import *
from .forms import LoginForm, RegistrationUserForm, PostForm
from .mixins import CategoryDetailMixin


class Index_View(TemplateView):
    
    template_name = "index.html"


class WineView(TemplateView):
    
    template_name = 'wine.html'


class StillWineView(TemplateView):
    
    template_name = 'still_wine.html'


class ForumView(ListView):
    
    model = Post
    template_name = 'forum.html'


class ForumPostDetailView(DetailView):
    
    model = Post
    template_name = 'forum_post_detail.html'
    

class AddPostVoew(CreateView):
    
    model = Post
    form_class = PostForm
    template_name = 'forum_post_add.html'
    # '__all__' добавляет к форме создания нового поста все поля, которые указаны в модели Post
    # fields = '__all__'
    # надо закомментировать строку fields(хоть она рабочая) лишь потому, что отныне будет использоваться
    # самостоятельно созданная форма PostForm
    # fields = ('title', 'body')


class LoginView(View):
    
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)


class RegistrationView(View):
    
    def get(self, request, *args, **kwargs):
        form = RegistrationUserForm(request.POST or None)
        context = {
            'form': form,
        }
        return render(request, 'registration.html', context)
    
    def post(self, request, *args, **kwargs):
        form = RegistrationUserForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
        context = {
            'form': form,
            }
        return render(request, 'registration.html', context)


class LogoutView(View):
    
    permanent = False

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')


class ProductDetailView(CategoryDetailMixin, DetailView):
    
    CT_MODEL_MODEL_CLASS = {
        'red_wine': Red_Wine,
        'rose_Wine': Rose_Wine,
        'white_Wine': White_Wine,
        'champagne': Champagne,
        'sparkling_wine': Sparkling_Wine,
        'porto': Porto,
        'bitter': Bitter,
        'vermouth': Vermouth,
        'whiskey': Whiskey,
        'rum': Rum,
        'tequila': Tequila,
        'mezcal': Mezcal,
        'gin': Gin,
        'vodka': Vodka,
        'liquor': Liquor,
        'cocktail': Cocktail,
    }

    def dispatch(self, request, *args, **kwargs):

        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ct_model'] = self.model._meta.model_name
        return context


class CategoryDetailView(CategoryDetailMixin, DetailView):
    
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart
        return context


