from PIL import Image

from django.forms import forms
from django.forms import ModelChoiceField, ModelForm
from django.core.exceptions import ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


# create a restriction on uploading too small images through the admin form
# (that is, if you upload images through the admin panel)

class AnyProductAdminForm(ModelForm):
    
    list_display = ("title")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # <span_style> turns the code into HTML and renders it according to the tags that are passed
        self.fields['image'].help_text = mark_safe(
            '<span style="color:#79aec8;">Notice! Please upload an image with no less than {}x{} px resolution</span>'.format(
                *Product.MIN_RESOLUTION
            )
        )
    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Uploaded image size exceeded! Acceptable value is not more than 3MB.')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Uploaded image size does not match the specified requirements!')
        if img.height > max_height or img.width > max_width:
            raise ValidationError('Uploaded image size does not match the specified requirements!')

        return image

# exclude the possibility of providing another choice when determining the category of the corresponding product (for biographies - only biography category, etc.)
class Red_Wine_Admin(admin.ModelAdmin):

    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='red_wine'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Rose_Wine_Admin(admin.ModelAdmin):
    
    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='rose_wine'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class White_Wine_Admin(admin.ModelAdmin):
    
    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='white_wine'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Champagne_Admin(admin.ModelAdmin):
    
    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='champagne'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Sparkling_Wine_Admin(admin.ModelAdmin):
    
    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='sparkling_wine'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Porto_Admin(admin.ModelAdmin):
    
    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='porto'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Bitter_Admin(admin.ModelAdmin):
    
    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='bitter'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Vermouth_Admin(admin.ModelAdmin):
    
    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='vermouth'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Whiskey_Admin(admin.ModelAdmin):
    
    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='whiskey'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Rum_Admin(admin.ModelAdmin):
    
    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='rum'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Tequila_Admin(admin.ModelAdmin):
    
    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='tequila'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Mezcal_Admin(admin.ModelAdmin):
    
    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='mezcal'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Gin_Admin(admin.ModelAdmin):
    
    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='gin'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Vodka_Admin(admin.ModelAdmin):
    
    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='vodka'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Liquor_Admin(admin.ModelAdmin):
    
    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='liquor'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Cocktail_Admin(admin.ModelAdmin):
    
    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='cocktail'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Red_Wine, Red_Wine_Admin)
admin.site.register(Rose_Wine, Rose_Wine_Admin)
admin.site.register(White_Wine, White_Wine_Admin)
admin.site.register(Champagne, Champagne_Admin)
admin.site.register(Sparkling_Wine, Sparkling_Wine_Admin)
admin.site.register(Porto, Porto_Admin)
admin.site.register(Bitter, Bitter_Admin)
admin.site.register(Vermouth, Vermouth_Admin)
admin.site.register(Whiskey, Whiskey_Admin)
admin.site.register(Rum, Rum_Admin)
admin.site.register(Tequila, Tequila_Admin)
admin.site.register(Mezcal, Mezcal_Admin)
admin.site.register(Gin, Gin_Admin)
admin.site.register(Vodka, Vodka_Admin)
admin.site.register(Liquor, Liquor_Admin)
admin.site.register(Cocktail, Cocktail_Admin)