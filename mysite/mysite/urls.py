import os

from django.urls import include,path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500, handler403, handler400
from django.contrib import admin

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('products/', include('django.contrib.auth.urls')),
    path('products/', include('products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'mysite.views.custom_page_not_found_view'
handler500 = 'mysite.views.custom_error_view'
handler403 = 'mysite.views.custom_permission_denied_view'
handler400 = 'mysite.views.custom_bad_request_view'