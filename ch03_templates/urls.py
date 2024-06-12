"""
URL configuration for djangoexercises project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from ch03_templates import views

urlpatterns = [
    path('ex01/', views.ex01, name='ex01'),
    path('ex02/', views.ex02, name='ex02'),
    path('ex03/', views.ex03, name='ex03'),
    path('ex04/', views.ex04, name='ex04'),
    path('ex05/', views.ex05, name='ex05'),
]
