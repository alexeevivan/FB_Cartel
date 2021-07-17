from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect, request
from django.views.generic import DetailView, View, ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import PostForm, ForumPostUpdateForm
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
    ordering = ['-pub_date']
    # перед добавлением datetime сортировка происходила по автоматически создаваемому Django id, который
    # добавлялся к каждому посту
    #ordering = ['-id']


class ForumPostDetailView(DetailView):
    
    model = Post
    template_name = 'forum_post_detail.html'
    

class AddPostView(CreateView):
    
    model = Post
    form_class = PostForm
    template_name = 'forum_post_add.html'
    # '__all__' добавляет к форме создания нового поста все поля, которые указаны в модели Post
    # fields = '__all__'
    # надо закомментировать строку fields(хоть она рабочая) лишь потому, что отныне будет использоваться
    # самостоятельно созданная форма PostForm
    # fields = ('title', 'body')


class UpdatePostView(UpdateView):
    
    model = Post
    form_class = ForumPostUpdateForm
    template_name = 'forum_post_update.html'


class RemovePostView(DeleteView):
    
    model = Post
    template_name = 'forum_post_remove.html'
    success_url = reverse_lazy('forum')


def PostCategoryView(request, categories):
    
    # post_category - характеристика категорий в модели Post, приравнивается в данном случае к записи в urls
    # (<str:categories>)
    category_posts = Post.objects.filter(post_category=categories)
    return render(request, 'post_categories.html', {'categories':categories.title, 'category_posts':category_posts})


class AddPostCategoryView(CreateView):
    
    model = PostCategory
    template_name = 'forum_post_category_add.html'
    fields = '__all__'
    success_url = reverse_lazy('forum')


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


