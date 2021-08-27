from django.urls import path, include
from . import views
from .views import *



urlpatterns = [
    path('', Index_View.as_view(), name='index'),
    path('forum', ForumView.as_view(), name='forum'),
    path('forum/forum_post_detail/<int:pk>', ForumPostDetailView.as_view(), name='forum_post_detail'),
    path('forum/forum_post_add/', AddPostView.as_view(), name='forum_post_add'),
    path('forum/forum_post_category_add/', AddPostCategoryView.as_view(), name='forum_post_category_add'),
    path('forum/forum_post_update/<int:pk>', UpdatePostView.as_view(), name='forum_post_update'),
    path('forum/like/<int:pk>', ForumPostLikeView, name='forum_post_like'),
    path('forum/<int:pk>/remove', RemovePostView.as_view(), name='forum_post_remove'),
    path('forum_post_detail/<int:pk>/forum_comment_add/ ', AddCommentView.as_view(), name='forum_post_comment_add'),
    path('category/<str:categories>/', PostCategoryView, name='category'),
    path('wine', WineView.as_view(), name='wine'),
    path('wine/still_wine', StillWineView.as_view(), name='still_wine'),
    path('captcha/', include('captcha.urls')),
    path('library/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),  
]