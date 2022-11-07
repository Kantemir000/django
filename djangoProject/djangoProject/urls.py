"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from firstap import views
""""""
urlpatterns = [
    re_path(r'^product/(?P<productid>\d+)/', views.products),
    re_path(r'^product/$', views.products), 
    re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
    path('', views.index, name='homa'),
    re_path(r'^about', views.about),
    re_path(r'^contact', views.contact),
    path('admin/', admin.site.urls)
]
