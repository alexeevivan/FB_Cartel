from django.urls import path, include
from .views import *


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile_edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('password/', PasswordEditView.as_view()),
]