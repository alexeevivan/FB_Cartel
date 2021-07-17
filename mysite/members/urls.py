from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
]