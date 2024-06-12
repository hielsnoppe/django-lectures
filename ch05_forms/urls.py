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

from ch05_forms import views

urlpatterns = [
    path('posts/create_fbv', views.ex01_post_create, name='post_create_fbv'),
    path('posts/create_cbv', views.PostCreateView.as_view(), name='post_create_cbv'),
]
