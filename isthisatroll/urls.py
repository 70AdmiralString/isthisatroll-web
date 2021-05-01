"""isthisatroll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.shortcuts import render

from user.views import SearchView

urlpatterns = [
    path('', SearchView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about')
]


def handler404(request, exception):
    """View for error 404."""
    response = render(request, '404.html')
    response.status_code = 404
    return response


def handler500(request):
    """View for error 500."""
    response = render(request, '500.html')
    response.status_code = 500
    return response
