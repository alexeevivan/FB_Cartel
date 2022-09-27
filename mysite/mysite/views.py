from django.shortcuts import render
from django.http import HttpResponse


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def custom_error_view(request, exception=None):
    return render(request, "500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})