from django.contrib import admin

from .models import *


admin.site.register(Post)
# admin.site.register(IpModel)
admin.site.register(Comment)
admin.site.register(PostCategory)
admin.site.register(Profile)