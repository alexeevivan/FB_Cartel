from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', Index_View.as_view(), name='index'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('forum', ForumView.as_view(), name='forum'),
    path('forum/forum_post_detail/<int:pk>', ForumPostDetailView.as_view(), name='forum_post_detail'),
    path('forum/forum_post_add/', AddPostVoew.as_view(), name='forum_post_add'),
    path('wine', WineView.as_view(), name='wine'),
    path('wine/still_wine', StillWineView.as_view(), name='still_wine'),
    path('captcha/', include('captcha.urls')),
    path('<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('library/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),  
]