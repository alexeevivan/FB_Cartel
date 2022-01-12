from PIL import Image

from django.db import models
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models.deletion import CASCADE
from django.http import HttpResponseRedirect, request
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from ckeditor.fields import RichTextField


class Post(models.Model):
    
    title = models.CharField(max_length=255, verbose_name='Название')
    author = models.ForeignKey(User, on_delete=CASCADE, verbose_name='Автор поста')
    body = RichTextField(blank=True, null=True, verbose_name = 'Сообщение')
    # Закомментировал вариант без RichTextField, который добавляет строку со эмодзи и т.д.
    # body = models.TextField(verbose_name='Сообщение')
    slug = models.SlugField(default='', editable=False,  max_length=160)
    uploaded_image = models.ImageField(null=True, blank=True, upload_to="img/")
    short_description = models.CharField(max_length=50, default='', verbose_name='Краткое описание поста')
    pub_date = models.DateField(auto_now_add=True)
    post_category = models.CharField(max_length=30, default='Рецептуры напитков', verbose_name='Категория')
    like = models.ManyToManyField(User, related_name='blog_posts')
    views = models.ManyToManyField(User, related_name='view_posts')
    
    def total_likes(self):
        return self.like.count()
    
    def total_views(self):
        return self.views.count()

    def get_absolute_url(self):
        return reverse("forum_post_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title + '|' + str(self.author)
    
    class Meta:
        
        ordering = ('-pub_date',)


class PostCategory(models.Model):
    
    name = models.CharField(max_length=30, verbose_name='Название категории')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("forum_post_detail", kwargs={"pk": self.pk})


class Profile(models.Model):
    
    user = models.OneToOneField(User, null=True, on_delete=CASCADE)
    bio = models.TextField()
    workplace = models.CharField(null=True, blank=True, max_length=255)
    profile_img = models.ImageField(null=True, blank=True, upload_to="img/profile")
    instagram_url = models.CharField(null=True, blank=True, max_length=255)
    vk_url = models.CharField(null=True, blank=True, max_length=255)
    facebook_url = models.CharField(null=True, blank=True, max_length=255)
    twitter_url  = models.CharField(null=True, blank=True, max_length=255)

    
    def __str__(self):
        return str(self.user)

    # для того, чтобы был редирект после того, как профиль создается вручную на сайте после регистрации
    def get_absolute_url(self):
        return reverse('index')


class Comment(models.Model):
    
    post = models.ForeignKey(Post, related_name='comments', on_delete=CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self, **kwargs):
        return '%s - %s' % (self.post.title, self.name)
    
    def get_absolute_url(self):
        return reverse("forum_post_detail", kwargs={"pk": self.post.pk})