from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'Blog/blog_list.html', context)

def blog_detail(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/blog_detail.html', context)