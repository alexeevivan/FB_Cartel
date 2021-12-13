from PIL import Image

from django.forms import forms
from django.forms import ModelChoiceField, ModelForm
from django.core.exceptions import ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostCategory)
admin.site.register(Profile)