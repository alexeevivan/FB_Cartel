from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('products', views.info_products, name='products'),
    path('products/products_list', views.info_products_list, name='products_list'),
    path('products/white_wine', views.info_white_wine, name='white_wine'),
    path('products/rose_wine', views.info_rose_wine, name='rose_wine'),
    path('products/red_wine', views.info_red_wine, name='red_wine'),
    path('products/sparkling_wine', views.info_sparkling_wine, name='sparkling_wine'),
    path('products/champagne', views.info_champagne, name='champagne'),
    path('products/bitter', views.info_bitter, name='bitter'),
    path('products/vermouth', views.info_vermouth, name='vermouth'),
    path('products/porto', views.info_porto, name='porto'),
    path('products/whiskey', views.info_whiskey, name='whiskey'),
    path('products/rum', views.info_rum, name='rum'),
    path('products/tequila', views.info_tequila, name='tequila'),
    path('products/mezcal', views.info_mezcal, name='mezcal'),
    path('products/liquor', views.info_liquor, name='liquor'),
    path('products/gin', views.info_gin, name='gin'),
    path('products/vodka', views.info_vodka, name='vodka'),
    path('products/cocktail', views.info_cocktail, name='cocktail'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results')
]