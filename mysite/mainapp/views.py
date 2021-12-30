from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect, request
from django.views.generic import TemplateView, DetailView, View, ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import PostForm, ForumPostUpdateForm, ForumPostCategoryAdd

from django.utils.decorators import method_decorator


class Index_View(TemplateView):
    
    template_name = "index.html"


class WineView(TemplateView):
    
    template_name = 'wine.html'


class AboutUsView(TemplateView):
    
    template_name = 'about.html'


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

    def get_context_data(self, *args, **kwargs):
        
        context = super(ForumPostDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.like.filter(id=self.request.user.id).exists():
            liked = True
        
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


def post_detail(self, request, *args, **kwargs):
    # Проверяем есть ли пост с запрашиваемым слагом
    post = get_object_or_404(Post, kwargs={"pk": self.pk})

    if not request.session.session_key:
        request.session.save()
    # получаем сессию
    session_key = request.session.session_key

    is_views = PostCountViews.objects.filter(postId=post.id, sesId=session_key)

    # если нет информации о просмотрах создаем ее
    if is_views.count() == 0 and str(session_key) != 'None':

        views = PostCountViews()
        views.sesId = session_key
        views.postId = post
        views.save()

        post.count_views += 1
        post.save()

    return render(request, 'forum_post_detail.html', context={'post': post})

    
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


def ForumPostLikeView(request, pk):
    
    # 'post id' - имя у кнопки в forum_post_detail
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
        liked = False
    else:
        post.like.add(request.user)
        liked = True 
    return HttpResponseRedirect(reverse('forum_post_detail', args=[str(pk)]))


def PostCategoryView(request, categories):
    
    # post_category - характеристика категорий в модели Post, приравнивается в данном случае к записи в urls
    # (<str:categories>)
    # replace функция заменяет все, что необходимо, требуя аргумент "на что менять" и "что именно менять"
    # в нашем случае менять нужно пробел на тире
    category_posts = Post.objects.filter(post_category=categories.replace('-', '%20'))
    return render(request, 'post_categories.html', {'categories':categories.title().replace('-', '%20'), 'category_posts':category_posts})


class AddPostCategoryView(CreateView):
    
    model = PostCategory
    form_class = ForumPostCategoryAdd
    template_name = 'forum_post_category_add.html'
    #fields = '__all__'
    success_url = reverse_lazy('forum')


class AddCommentView(CreateView):
    
    model = Comment
    template_name = 'forum_post_comment_add.html'
    fields = '__all__'


# def get_client_ip(request):
    
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip