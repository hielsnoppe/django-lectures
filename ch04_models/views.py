from django.shortcuts import render

from .models import Category, Post

# Create your views here.

def ex01_post_list(request):
    posts = Post.objects.all()
    #posts = Post.objects.order_by('-title')
    context = {
        'posts_list': posts
    }
    return render(
        request,
        'ch04/ex01_post_list.html',
        context
        )

def ex02_post_detail(request, id):
    post = Post.objects.get(pk=id)
    context = {
        'post': post
    }
    return render(
        request,
        'ch04/ex02_post_detail.html',
        context
    )

def ex03_category_detail(request, id):
    category = Category.objects.get(pk=id)
    context = {
        'category': category
    }
    return render(
        request,
        'ch04/ex03_category_detail.html',
        context
    )