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
class Red_wine_Admin(admin.ModelAdmin):

    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='red_wine'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Rose_wine_Admin(admin.ModelAdmin):
    
    form = AnyProductAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='rose_wine'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class White_wine_Admin(admin.ModelAdmin):
    
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

# Register your models here.
admin.site.register(Category)
admin.site.register(Red_wine, Red_wine_Admin)
admin.site.register(Rose_wine, Rose_wine_Admin)
admin.site.register(White_wine, White_wine_Admin)
admin.site.register(Champagne, Champagne_Admin)