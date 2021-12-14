from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('library/', views.info_library, name='library'),
    path('library/products_list', views.info_products_list, name='products_list'),
    path('library/white_wine', views.info_white_wine, name='white_wine'),
    path('library/rose_wine', views.info_rose_wine, name='rose_wine'),
    path('library/red_wine', views.info_red_wine, name='red_wine'),
    path('library/sparkling_wine', views.info_sparkling_wine, name='sparkling_wine'),
    path('library/champagne', views.info_champagne, name='champagne'),
    path('library/bitter', views.info_bitter, name='bitter'),
    path('library/vermouth', views.info_vermouth, name='vermouth'),
    path('library/porto', views.info_porto, name='porto'),
    path('library/whiskey', views.info_whiskey, name='whiskey'),
    path('library/rum', views.info_rum, name='rum'),
    path('library/tequila', views.info_tequila, name='tequila'),
    path('library/mezcal', views.info_mezcal, name='mezcal'),
    path('library/liquor', views.info_liquor, name='liquor'),
    path('library/gin', views.info_gin, name='gin'),
    path('library/vodka', views.info_vodka, name='vodka'),
    path('library/cocktail', views.info_cocktail, name='cocktail'),
    path('<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('library/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results')
]