from django.urls import path, include
from . import views
from .views import *
from .decorators import check_recaptcha


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', check_recaptcha(views.UserLoginView.as_view()), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile_edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('profile_page_create/', ProfilePageCreateView.as_view(), name='profile_page_create'),
    path('password/', PasswordEditView.as_view()),
    path('<int:pk>/profile/', ProfileShowPageView.as_view(), name='profile_page'),
    path('<int:pk>/profile_edit_page/', ProfileEditPageView.as_view(), name='profile_edit_page'),
]