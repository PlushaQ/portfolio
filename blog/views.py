from django.shortcuts import render
from .models import Blog
# Create your views here.


def all_posts(request):
    blog_posts = Blog.objects
    return render(request, 'blog/all_posts.html', {'blog_posts': blog_posts})
