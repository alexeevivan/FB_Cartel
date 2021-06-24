from django.urls import path, include
from . import views
from .views import Index_View, LoginView, RegistrationView, LogoutView, ProductDetailView, CategoryDetailView, WineView

urlpatterns = [
    path('', Index_View.as_view(), name='index'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('wine', WineView.as_view(), name='wine'),
    path('captcha/', include('captcha.urls')),
    path('<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('library/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),  
]