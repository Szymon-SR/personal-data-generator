"""data_generation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from addresses import views as addresses_views
from names import views as names_views
from .views import generation_view, home_view, file_view, about_view

urlpatterns = [
    path("", home_view, name="home"),
    path("generation/", generation_view, name="generation"),
    path("generation/gender<str:gender>/", generation_view, name="generation_gender"),
    path("to_file/", file_view, name="to_file"),
    path("admin/", admin.site.urls),
    path("about/", about_view, name="about"),
    path("post_addresses/create", addresses_views.post_address_create_view),
    path("streets/create", addresses_views.street_address_create_view),
    path("first_names/create", names_views.first_name_create_view),
    path("last_names/create", names_views.last_name_create_view),
]
