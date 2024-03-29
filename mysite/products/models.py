from PIL import Image

from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from datetime import date, datetime

def get_models_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]

def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class MinResolutionErrorException(Exception):
    pass


class MaxResolutionErrorException(Exception):
    pass


class LatestProductsManager:
    
    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:1]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )
        return products


class LatestProducts:
    
    objects = LatestProductsManager()


class CategoryManager(models.Manager):
    
    CATEGORY_NAME_COUNT_NAME = {
        'Red_Wine': 'red_wine__count',
        'Rose_Wine': 'rose_wine__count',
        'White_Wine': 'white_wine__count',
        'Champagne': 'champagne__count',
        'Sparkling_Wine': 'sparkling_wine__count',
        'Porto': 'porto__count',
        'Bitter': 'bitter__count',
        'Vermouth': 'vermouth__count',
        'Whiskey': 'whiskey__count',
        'Rum': 'Rum__count',
        'Tequila': 'tequila__count',
        'Mezcal': 'mezcal__count',
        'Gin': 'gin__count',
        'Vodka': 'vodka__count',
        'Liquor': 'liquor__count',
        'Cocktail': 'cocktail__count',
    }


    def get_queryset(self):
        return super().get_queryset()

    def get_categories_for_left_sidebar(self):
        models = get_models_for_count('red_wine', 'rose_wine', 'white_wine', 'champagne', 'sparkling_wine',
                                      'porto', 'bitter', 'vermouth', 'whiskey', 'rum', 'tequila', 'mezcal',
                                      'gin', 'vodka', 'liquor', 'cocktail')
        qs = list(self.get_queryset().annotate(*models))
        data = [
            dict(name=c.name, url=c.get_absolute_url(), count=getattr(c, self.CATEGORY_NAME_COUNT_NAME[c.name]))
            for c in qs
        ]
        return data


class Category(models.Model):
    
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(unique=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Product(models.Model):
    
    MIN_RESOLUTION = (400,400)
    MAX_RESOLUTION = (4000,4000)
    MAX_IMAGE_SIZE = 3145728


    class Meta:
        abstract=True
    

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование продукции')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null = True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена', null=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        image = self.image
        img = Image.open(image)
        min_height, min_width = self.MIN_RESOLUTION
        max_height, max_width = self.MAX_RESOLUTION
        if img.height < min_height or img.width < min_width:
            raise MinResolutionErrorException('Uploaded image size does not match the specified requirements!')
        if img.height > max_height or img.width > max_width:
            raise MaxResolutionErrorException('Uploaded image size does not match the specified requirements!')
        super().save(*args, **kwargs)

    def get_model_name(self):
        return self.__class__.__name__.lower()


class Red_Wine(Product):
    
    spirit_type = models.CharField(max_length=255, verbose_name='Категория:')
    region = models.CharField(max_length=255, verbose_name='Регион производства:', null=False, blank=False)
    vintage = models.CharField(max_length=10, verbose_name='Винтаж:')
    alcohol = models.CharField(max_length=10, verbose_name='Крепость:')
    value = models.CharField(max_length=10, verbose_name='Объём:')
    grape = models.CharField(max_length=255, verbose_name='Виноград')
    color = models.CharField(max_length=255, verbose_name='Цвет:')
    flavour = models.CharField(max_length=255, verbose_name='Аромат:')
    taste = models.CharField(max_length=255, verbose_name='Вкус:')
    body = models.CharField(max_length=10, verbose_name='Тело')
    gastronomic = models.TextField(max_length=255, verbose_name='Гастрономическое сочетание:')
    cocktails = models.CharField(max_length=255, verbose_name="Входит в состав коктейлей:", null=True)
    serving = models.CharField(max_length=255, verbose_name='Температура сервировки:')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель:')
    manufacturer_site = models.CharField(max_length=255, verbose_name='Сайт производителя')
    provider = models.CharField(max_length=255, verbose_name='Поставщик:', null=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Rose_Wine(Product):
    
    spirit_type = models.CharField(max_length=255, verbose_name='Категория:')
    region = models.CharField(max_length=255, verbose_name='Регион производства:', null=False, blank=False)
    vintage = models.CharField(max_length=10, verbose_name='Винтаж:')
    alcohol = models.CharField(max_length=10, verbose_name='Крепость:')
    value = models.CharField(max_length=10, verbose_name='Объём:')
    grape = models.CharField(max_length=255, verbose_name='Виноград')
    color = models.CharField(max_length=255, verbose_name='Цвет:')
    flavour = models.CharField(max_length=255, verbose_name='Аромат:')
    taste = models.CharField(max_length=255, verbose_name='Вкус:')
    body = models.CharField(max_length=10, verbose_name='Тело')
    gastronomic = models.TextField(max_length=255, verbose_name='Гастрономическое сочетание:')
    cocktails = models.CharField(max_length=255, verbose_name="Входит в состав коктейлей:", null=True)
    serving = models.CharField(max_length=255, verbose_name='Температура сервировки:')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель:')
    manufacturer_site = models.CharField(max_length=255, verbose_name='Сайт производителя')
    provider = models.CharField(max_length=255, verbose_name='Поставщик:', null=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class White_Wine(Product):
    
    spirit_type = models.CharField(max_length=255, verbose_name='Категория:')
    region = models.CharField(max_length=255, verbose_name='Регион производства:', null=False, blank=False)
    vintage = models.CharField(max_length=10, verbose_name='Винтаж:')
    alcohol = models.CharField(max_length=10, verbose_name='Крепость:')
    value = models.CharField(max_length=10, verbose_name='Объём:')
    grape = models.CharField(max_length=255, verbose_name='Виноград')
    color = models.CharField(max_length=255, verbose_name='Цвет:')
    flavour = models.CharField(max_length=255, verbose_name='Аромат:')
    taste = models.CharField(max_length=255, verbose_name='Вкус:')
    body = models.CharField(max_length=10, verbose_name='Тело')
    gastronomic = models.TextField(max_length=255, verbose_name='Гастрономическое сочетание:')
    cocktails = models.CharField(max_length=255, verbose_name="Входит в состав коктейлей:", null=True)
    serving = models.CharField(max_length=255, verbose_name='Температура сервировки:')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель:')
    manufacturer_site = models.CharField(max_length=255, verbose_name='Сайт производителя')
    provider = models.CharField(max_length=255, verbose_name='Поставщик:', null=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Champagne(Product):
    
    spirit_type = models.CharField(max_length=255, verbose_name='Категория:')
    country_of_manufacturing = models.CharField(max_length=255, verbose_name='Страна производства')
    region = models.CharField(max_length=255, verbose_name='Регион производства:')
    vintage = models.CharField(max_length=10, verbose_name='Винтаж:')
    alcohol = models.CharField(max_length=10, verbose_name='Крепость:')
    value = models.CharField(max_length=10, verbose_name='Объём:')
    grape = models.CharField(max_length=255, verbose_name='Виноград')
    color = models.CharField(max_length=255, verbose_name='Цвет:')
    flavour = models.CharField(max_length=255, verbose_name='Аромат:')
    taste = models.CharField(max_length=255, verbose_name='Вкус:')
    body = models.CharField(max_length=10, verbose_name='Тело')
    gastronomic = models.CharField(max_length=13, verbose_name='Гастрономическое сочетание:')
    cocktails = models.CharField(max_length=255, verbose_name="Входит в состав коктейлей:", null=True)
    serving = models.CharField(max_length=255, verbose_name='Температура сервировки:')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель:')
    manufacturer_site = models.CharField(max_length=255, verbose_name='Сайт производителя')
    provider = models.CharField(max_length=255, verbose_name='Поставщик:', null=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Sparkling_Wine(Product):
    
    spirit_type = models.CharField(max_length=255, verbose_name='Категория:')
    country_of_manufacturing = models.CharField(max_length=255, verbose_name='Страна производства')
    region = models.CharField(max_length=255, verbose_name='Регион производства:')
    vintage = models.CharField(max_length=10, verbose_name='Винтаж:')
    alcohol = models.CharField(max_length=10, verbose_name='Крепость:')
    value = models.CharField(max_length=10, verbose_name='Объём:')
    grape = models.CharField(max_length=255, verbose_name='Виноград')
    color = models.CharField(max_length=255, verbose_name='Цвет:')
    flavour = models.CharField(max_length=255, verbose_name='Аромат:')
    taste = models.CharField(max_length=255, verbose_name='Вкус:')
    body = models.CharField(max_length=10, verbose_name='Тело')
    gastronomic = models.TextField(max_length=255, verbose_name='Гастрономическое сочетание:')
    cocktails = models.CharField(max_length=255, verbose_name="Входит в состав коктейлей:", null=True)
    serving = models.CharField(max_length=255, verbose_name='Температура сервировки:')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель:')
    manufacturer_site = models.CharField(max_length=255, verbose_name='Сайт производителя')
    provider = models.CharField(max_length=255, verbose_name='Поставщик:', null=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Porto(Product):
    
    spirit_type = models.CharField(max_length=255, verbose_name='Категория:')
    country_of_manufacturing = models.CharField(max_length=255, verbose_name='Страна производства')
    region = models.CharField(max_length=255, verbose_name='Регион производства:')
    vintage = models.CharField(max_length=10, verbose_name='Винтаж:', null=True)
    alcohol = models.CharField(max_length=10, verbose_name='Крепость:')
    value = models.CharField(max_length=10, verbose_name='Объём:')
    grape = models.CharField(max_length=255, verbose_name='Виноград')
    color = models.CharField(max_length=255, verbose_name='Цвет:')
    flavour = models.CharField(max_length=255, verbose_name='Аромат:')
    taste = models.CharField(max_length=255, verbose_name='Вкус:')
    body = models.CharField(max_length=10, verbose_name='Тело')
    gastronomic = models.TextField(max_length=255, verbose_name='Гастрономическое сочетание:')
    cocktails = models.CharField(max_length=255, verbose_name="Входит в состав коктейлей:", null=True)
    serving = models.CharField(max_length=255, verbose_name='Температура сервировки:')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель:')
    manufacturer_site = models.CharField(max_length=255, verbose_name='Сайт производителя')
    provider = models.CharField(max_length=255, verbose_name='Поставщик:', null=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Bitter(Product):
    
    spirit_type = models.CharField(max_length=255, verbose_name='Категория:')
    country_of_manufacturing = models.CharField(max_length=255, verbose_name='Страна производства')
    region = models.CharField(max_length=255, verbose_name='Регион производства:')
    vintage = models.CharField(max_length=10, verbose_name='Винтаж:', null=True)
    alcohol = models.CharField(max_length=10, verbose_name='Крепость:')
    value = models.CharField(max_length=10, verbose_name='Объём:')
    color = models.CharField(max_length=255, verbose_name='Цвет:')
    flavour = models.CharField(max_length=255, verbose_name='Аромат:')
    combination = models.CharField(max_length=255, verbose_name='Сочитается с:')
    cocktails = models.CharField(max_length=255, verbose_name="Входит в состав коктейлей:")
    serving = models.CharField(max_length=255, verbose_name='Температура сервировки:')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель:')
    manufacturer_site = models.CharField(max_length=255, verbose_name='Сайт производителя')
    provider = models.CharField(max_length=255, verbose_name='Поставщик:', null=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Vermouth(Product):
    
    spirit_type = models.CharField(max_length=255, verbose_name='Категория:')
    country_of_manufacturing = models.CharField(max_length=255, verbose_name='Страна производства')
    region = models.CharField(max_length=255, verbose_name='Регион производства:')
    vintage = models.CharField(max_length=10, verbose_name='Винтаж:', null=True)
    alcohol = models.CharField(max_length=10, verbose_name='Крепость:')
    value = models.CharField(max_length=10, verbose_name='Объём:')
    color = models.CharField(max_length=255, verbose_name='Цвет:')
    flavour = models.CharField(max_length=255, verbose_name='Аромат:')
    combination = models.CharField(max_length=255, verbose_name='Сочитается с:')
    cocktails = models.CharField(max_length=255, verbose_name="Входит в состав коктейлей:")
    serving = models.CharField(max_length=255, verbose_name='Температура сервировки:')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель:')
    manufacturer_site = models.CharField(max_length=255, verbose_name='Сайт производителя')
    provider = models.CharField(max_length=255, verbose_name='Поставщик:', null=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')
    

class Whiskey(Product):
    
    spirit_type = models.CharField(max_length=255, verbose_name='Категория:')
    country_of_manufacturing = models.CharField(max_length=255, verbose_name='Страна производства')
    region = models.CharField(max_length=255, verbose_name='Регион производства:')
    vintage = models.CharField(max_length=10, verbose_name='Винтаж:', null=True)
    alcohol = models.CharField(max_length=10, verbose_name='Крепость:')
    value = models.CharField(max_length=10, verbose_name='Объём:')
    color = models.CharField(max_length=255, verbose_name='Цвет:')
    flavour = models.CharField(max_length=255, verbose_name='Аромат:')
    combination = models.CharField(max_length=255, verbose_name='Сочитается с:')
    cocktails = models.CharField(max_length=255, verbose_name="Входит в состав коктейлей:")
    serving = models.CharField(max_length=255, verbose_name='Температура сервировки:')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель:')
    manufacturer_site = models.CharField(max_length=255, verbose_name='Сайт производителя')
    provider = models.CharField(max_length=255, verbose_name='Поставщик:', null=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')
    

class Rum(Product):
    
    spirit_type = models.CharField(max_length=255, verbose_name='Категория:')
    country_of_manufacturing = models.CharField(max_length=255, verbose_name='Страна производства')
    region = models.CharField(max_length=255, verbose_name='Регион производства:')
    vintage = models.CharField(max_length=10, verbose_name='Винтаж:', null=True)
    alcohol = models.CharField(max_length=10, verbose_name='Крепость:')
    value = models.CharField(max_length=10, verbose_name='Объём:')
    color = models.CharField(max_length=255, verbose_name='Цвет:')
    flavour = models.CharField(max_length=255, verbose_name='Аромат:')
    combination = models.CharField(max_length=255, verbose_name='Сочитается с:')
    cocktails = models.CharField(max_length=255, verbose_name="Входит в состав коктейлей:")
    serving = models.CharField(max_length=255, verbose_name='Температура сервировки:')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель:')
    manufacturer_site = models.CharField(max_length=255, verbose_name='Сайт производителя')
    provider = models.CharField(max_length=255, verbose_name='Поставщик:', null=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Tequila(Product):
    
    spirit_type = models.CharField(max_length=255, verbose_name='Категория:')
    country_of_manufacturing = models.CharField(max_length=255, verbose_name='Страна производства')
    region = models.CharField(max_length=255, verbose_name='Регион производства:')
    vintage = models.CharField(max_length=10, verbose_name='Винтаж:', null=True)
    alcohol = models.CharField(max_length=10, verbose_name='Крепость:')
    value = models.CharField(max_length=10, verbose_name='Объём:')
    color = models.CharField(max_length=255, verbose_name='Цвет:')
    flavour = models.CharField(max_length=255, verbose_name='Аромат:')
    combination = models.CharField(max_length=255, verbose_name='Сочитается с:')
    cocktails = models.CharField(max_length=255, verbose_name="Входит в состав коктейлей:")
    serving = models.CharField(max_length=255, verbose_name='Температура сервировки:')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель:')
    manufacturer_site = models.CharField(max_length=255, verbose_name='Сайт производителя')
    provider = models.CharField(max_length=255, verbose_name='Поставщик:', null=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Mezcal(Product):
    
    spirit_type = models.CharField(max_length=255, verbose_name='Категория:')
    country_of_manufacturing = models.CharField(max_length=255, verbose_name='Страна производства')
    region = models.CharField(max_length=255, verbose_name='Регион производства:')
    vintage = models.CharField(max_length=10, verbose_name='Винтаж:', null=True)
    alcohol = models.CharField(max_length=10, verbose_name='Крепость:')
    value = models.CharField(max_length=10, verbose_name='Объём:')
    color = models.CharField(max_length=255, verbose_name='Цвет:')
    flavour = models.CharField(max_length=255, verbose_name='Аромат:')
    combination = models.CharField(max_length=255, verbose_name='Сочитается с:')
    cocktails = models.CharField(max_length=255, verbose_name="Входит в состав коктейлей:")
    serving = models.CharField(max_length=255, verbose_name='Температура сервировки:')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель:')
    manufacturer_site = models.CharField(max_length=255, verbose_name='Сайт производителя')
    provider = models.CharField(max_length=255, verbose_name='Поставщик:', null=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Gin(Product):
    
    spirit_type = models.CharField(max_length=255, verbose_name='Категория:')
    country_of_manufacturing = models.CharField(max_length=255, verbose_name='Страна производства')
    region = models.CharField(max_length=255, verbose_name='Регион производства:')
    vintage = models.CharField(max_length=10, verbose_name='Винтаж:', null=True)
    alcohol = models.CharField(max_length=10, verbose_name='Крепость:')
    value = models.CharField(max_length=10, verbose_name='Объём:')
    color = models.CharField(max_length=255, verbose_name='Цвет:')
    flavour = models.CharField(max_length=255, verbose_name='Аромат:')
    combination = models.CharField(max_length=255, verbose_name='Сочитается с:')
    cocktails = models.CharField(max_length=255, verbose_name="Входит в состав коктейлей:")
    serving = models.CharField(max_length=255, verbose_name='Температура сервировки:')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель:')
    manufacturer_site = models.CharField(max_length=255, verbose_name='Сайт производителя')
    provider = models.CharField(max_length=255, verbose_name='Поставщик:', null=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Vodka(Product):
    
    spirit_type = models.CharField(max_length=255, verbose_name='Категория:')
    country_of_manufacturing = models.CharField(max_length=255, verbose_name='Страна производства')
    region = models.CharField(max_length=255, verbose_name='Регион производства:')
    alcohol = models.CharField(max_length=10, verbose_name='Крепость:')
    value = models.CharField(max_length=10, verbose_name='Объём:')
    color = models.CharField(max_length=255, verbose_name='Цвет:')
    flavour = models.CharField(max_length=255, verbose_name='Аромат:')
    combination = models.CharField(max_length=255, verbose_name='Сочитается с:')
    cocktails = models.CharField(max_length=255, verbose_name="Входит в состав коктейлей:")
    serving = models.CharField(max_length=255, verbose_name='Температура сервировки:')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель:')
    manufacturer_site = models.CharField(max_length=255, verbose_name='Сайт производителя')
    provider = models.CharField(max_length=255, verbose_name='Поставщик:', null=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Liquor(Product):
    
    spirit_type = models.CharField(max_length=255, verbose_name='Категория:')
    country_of_manufacturing = models.CharField(max_length=255, verbose_name='Страна производства')
    region = models.CharField(max_length=255, verbose_name='Регион производства:')
    vintage = models.CharField(max_length=10, verbose_name='Винтаж:', null=True)
    alcohol = models.CharField(max_length=10, verbose_name='Крепость:')
    value = models.CharField(max_length=10, verbose_name='Объём:')
    color = models.CharField(max_length=255, verbose_name='Цвет:')
    flavour = models.CharField(max_length=255, verbose_name='Аромат:')
    combination = models.CharField(max_length=255, verbose_name='Сочитается с:')
    cocktails = models.CharField(max_length=255, verbose_name="Входит в состав коктейлей:")
    serving = models.CharField(max_length=255, verbose_name='Температура сервировки:')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель:')
    manufacturer_site = models.CharField(max_length=255, verbose_name='Сайт производителя')
    provider = models.CharField(max_length=255, verbose_name='Поставщик:', null=True)

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Cocktail(Product):
    
    spirit_type = models.CharField(max_length=255, verbose_name='Категория:')
    alcohol = models.CharField(max_length=10, verbose_name='Крепость:')
    value = models.CharField(max_length=10, verbose_name='Объём:')
    color = models.CharField(max_length=255, verbose_name='Цвет:')
    flavour = models.CharField(max_length=255, verbose_name='Аромат:')
    manufacturer = models.CharField(max_length=255, verbose_name='История создания:')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')