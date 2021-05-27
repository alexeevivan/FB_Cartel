from django.views.generic.detail import SingleObjectMixin
from .models import Category, Red_wine, Rose_wine, White_wine, Champagne

class CategoryDetailMixin(SingleObjectMixin):
    
    CATEGORY_SLUG2PRODUCT_MODEL = {
        'red_wine': Red_wine,
        'rose_Wine': Rose_wine,
        'white_Wine': White_wine,
        'champagne': Champagne,
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