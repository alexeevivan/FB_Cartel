from django.views.generic.detail import SingleObjectMixin
from django.views.generic import View

from .models import Category, Red_Wine, Rose_Wine, Whiskey, White_Wine, Sparkling_Wine, Champagne, Porto, Bitter, Vermouth, Rum, Tequila, Mezcal, Gin, Vodka, Liquor, Cocktail

class CategoryDetailMixin(SingleObjectMixin):

    CATEGORY_SLUG2PRODUCT_MODEL = {
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

    def get_context_data(self, **kwargs):
        if isinstance(self.get_object(), Category):
            model = self.CATEGORY_SLUG2PRODUCT_MODEL[self.get_object().slug]
            context = super().get_context_data(**kwargs)
            context['categories'] = Category.objects.get_categories_for_left_sidebar()
            context['category_products'] = model.objects.all()
            return context
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.get_categories_for_left_sidebar()
        return context