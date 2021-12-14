from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
from .mixins import *


def info_library(request):
    return render(request, 'library.html', {})

def info_white_wine(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'white_wine'
    )
    return render(request, 'white_wine.html', {'categories': categories, 'products': products})

def info_rose_wine(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'rose_wine'
    )
    return render(request, 'rose_wine.html', {'categories': categories, 'products': products})

def info_red_wine(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'red_wine'
    )
    return render(request, 'red_wine.html', {'categories': categories, 'products': products})

def info_champagne(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'champagne'
    )
    return render(request, 'champagne.html', {'categories': categories, 'products': products})

def info_sparkling_wine(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'sparkling_wine'
    )
    return render(request, 'sparkling_wine.html', {'categories': categories, 'products': products})

def info_porto(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'porto'
    )
    return render(request, 'porto.html', {'categories': categories, 'products': products})

def info_bitter(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'bitter'
    )
    return render(request, 'bitter.html', {'categories': categories, 'products': products})

def info_vermouth(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'vermouth'
    )
    return render(request, 'vermouth.html', {'categories': categories, 'products': products})

def info_whiskey(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'whiskey'
    )
    return render(request, 'whiskey.html', {'categories': categories, 'products': products})

def info_rum(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'rum'
    )
    return render(request, 'rum.html', {'categories': categories, 'products': products})

def info_tequila(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'tequila'
    )
    return render(request, 'tequila.html', {'categories': categories, 'products': products})

def info_mezcal(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'mezcal'
    )
    return render(request, 'mezcal.html', {'categories': categories, 'products': products})

def info_gin(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'gin'
    )
    return render(request, 'gin.html', {'categories': categories, 'products': products})

def info_vodka(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'vodka'
    )
    return render(request, 'vodka.html', {'categories': categories, 'products': products})

def info_liquor(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'liquor'
    )
    return render(request, 'liquor.html', {'categories': categories, 'products': products})

def info_cocktail(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'cocktail'
    )
    return render(request, 'cocktail.html', {'categories': categories, 'products': products})

def info_products_list(request):
    categories = Category.objects.get_categories_for_left_sidebar()
    products = LatestProducts.objects.get_products_for_main_page(
        'white_wine', 'rose_wine', 'red_wine', 'champagne', 'sparkling_wine',
        'porto', 'bitter', 'vermouth', 'whiskey', 'rum', 'tequila', 'mezcal',
        'gin', 'vodka', 'liquor', 'cocktail', with_respect_to = 'white_wine'
    )
    return render(request, 'products_list.html', {'categories': categories, 'products': products})

class CategoryDetailView(CategoryDetailMixin, DetailView):
    
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart
        return context

# building a scheme, thats can help to show the url-address of each product
class ProductDetailView(CategoryDetailMixin, DetailView):
    
    CT_MODEL_MODEL_CLASS = {
        'red_wine': Red_Wine,
        'rose_wine': Rose_Wine,
        'white_wine': White_Wine,
        'champagne': Champagne,
        'sparkling_wine': Sparkling_Wine,
        'porto': Porto,
        'bitter': Bitter,
        'vermouth': Vermouth,
        'whiskey': Whiskey,
        'rum': Rum,
        'tequila': Tequila,
        'mezcal': Mezcal,
        'gin': Gin,
        'vodka': Vodka,
        'liquor': Liquor,
        'cocktail': Cocktail
    }

    def dispatch(self, request, *args, **kwargs):

        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ct_model'] = self.model._meta.model_name
        return context


class SearchResultsView(ListView):
    model = White_Wine, Rose_Wine, Red_Wine, Sparkling_Wine, Champagne, Porto, Bitter, Vermouth, Whiskey, Rum, Tequila, Mezcal, Gin, Vodka, Liquor, Cocktail
    template_name = 'search_results.html'
    def get_queryset(self):
            query = self.request.GET.get('q')
            object_list_1 = White_Wine.objects.filter(
                Q(title__icontains=query) | Q(spirit_type__icontains=query) | Q(region__icontains=query)
                | Q(vintage__icontains=query)  | Q(grape__icontains=query)  | Q(cocktails__icontains=query)
                | Q(manufacturer__icontains=query)  | Q(provider__icontains=query)
            )
            object_list_2 = Rose_Wine.objects.filter(
                Q(title__icontains=query) | Q(spirit_type__icontains=query) | Q(region__icontains=query)
                | Q(vintage__icontains=query)  | Q(grape__icontains=query)  | Q(cocktails__icontains=query)
                | Q(manufacturer__icontains=query)  | Q(provider__icontains=query)
            )
            object_list_3 = Red_Wine.objects.filter(
                Q(title__icontains=query) | Q(spirit_type__icontains=query) | Q(region__icontains=query)
                | Q(vintage__icontains=query)  | Q(grape__icontains=query)  | Q(cocktails__icontains=query)
                | Q(manufacturer__icontains=query) | Q(provider__icontains=query)
            )
            object_list_4 = Sparkling_Wine.objects.filter(
                Q(title__icontains=query) | Q(spirit_type__icontains=query) | Q(region__icontains=query)
                | Q(vintage__icontains=query) | Q(grape__icontains=query) | Q(cocktails__icontains=query)
                | Q(manufacturer__icontains=query) | Q(provider__icontains=query)
            )
            object_list_5 = Champagne.objects.filter(
                Q(title__icontains=query) | Q(spirit_type__icontains=query) | Q(region__icontains=query)
                | Q(vintage__icontains=query) | Q(grape__icontains=query) | Q(cocktails__icontains=query)
                | Q(manufacturer__icontains=query) | Q(provider__icontains=query)
            )
            object_list_6 = Porto.objects.filter(
                Q(title__icontains=query) | Q(spirit_type__icontains=query) | Q(region__icontains=query)
                | Q(vintage__icontains=query) | Q(grape__icontains=query) | Q(cocktails__icontains=query)
                | Q(manufacturer__icontains=query) | Q(provider__icontains=query)
            )
            object_list_7 = Bitter.objects.filter(
                Q(title__icontains=query) | Q(spirit_type__icontains=query) | Q(region__icontains=query)
                | Q(vintage__icontains=query) | Q(cocktails__icontains=query)
                | Q(manufacturer__icontains=query) | Q(provider__icontains=query)
            )
            object_list_8 = Vermouth.objects.filter(
                Q(title__icontains=query) | Q(spirit_type__icontains=query) | Q(region__icontains=query)
                | Q(vintage__icontains=query) | Q(cocktails__icontains=query)
                | Q(manufacturer__icontains=query) | Q(provider__icontains=query)
            )
            object_list_9 = Whiskey.objects.filter(
                Q(title__icontains=query) | Q(spirit_type__icontains=query) | Q(region__icontains=query)
                | Q(vintage__icontains=query) | Q(cocktails__icontains=query)
                | Q(manufacturer__icontains=query) | Q(provider__icontains=query)
            )
            object_list_10= Rum.objects.filter(
                Q(title__icontains=query) | Q(spirit_type__icontains=query) | Q(region__icontains=query)
                | Q(vintage__icontains=query) | Q(cocktails__icontains=query)
                | Q(manufacturer__icontains=query) | Q(provider__icontains=query)
            )
            object_list_11 = Tequila.objects.filter(
                Q(title__icontains=query) | Q(spirit_type__icontains=query) | Q(region__icontains=query)
                | Q(vintage__icontains=query) | Q(cocktails__icontains=query)
                | Q(manufacturer__icontains=query) | Q(provider__icontains=query)
            )
            object_list_12 = Mezcal.objects.filter(
                Q(title__icontains=query) | Q(spirit_type__icontains=query) | Q(region__icontains=query)
                | Q(vintage__icontains=query) | Q(cocktails__icontains=query)
                | Q(manufacturer__icontains=query) | Q(provider__icontains=query)
            )
            object_list_13 = Gin.objects.filter(
                Q(title__icontains=query) | Q(spirit_type__icontains=query) | Q(region__icontains=query)
                | Q(vintage__icontains=query) | Q(cocktails__icontains=query)
                | Q(manufacturer__icontains=query) | Q(provider__icontains=query)
            )
            object_list_14 = Vodka.objects.filter(
                Q(title__icontains=query) | Q(spirit_type__icontains=query) | Q(region__icontains=query)
                | Q(cocktails__icontains=query)
                | Q(manufacturer__icontains=query) | Q(provider__icontains=query)
            )
            object_list_15 = Liquor.objects.filter(
                Q(title__icontains=query) | Q(spirit_type__icontains=query) | Q(region__icontains=query)
                | Q(vintage__icontains=query) | Q(cocktails__icontains=query)
                | Q(manufacturer__icontains=query) | Q(provider__icontains=query)
            )
            object_list_16 = Cocktail.objects.filter(
                Q(title__icontains=query) | Q(manufacturer__icontains=query)
            )
            object_list = object_list_1, object_list_2, object_list_3, object_list_4, object_list_5, object_list_6, object_list_7, object_list_8, object_list_9, object_list_10, object_list_11, object_list_12, object_list_13, object_list_14, object_list_15, object_list_16
            return object_list_1 or object_list_2 or object_list_3 or object_list_4 or object_list_5 or object_list_6 or object_list_7 or object_list_8 or object_list_9 or object_list_10 or object_list_11 or object_list_12 or object_list_13 or object_list_14 or object_list_15 or object_list_16