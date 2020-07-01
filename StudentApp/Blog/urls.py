from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    path('', views.home, name='blog-list'),
    path('blog-detail/<int:blog_id>', views.blog_detail, name='blog-detail'),
]