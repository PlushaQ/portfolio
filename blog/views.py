from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def all_posts(request):
    blog_posts = Blog.objects
    return render(request, 'blog/all_posts.html', {'blog_posts': blog_posts})


def blog_post(request, blog_id):
    blog_post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_post.html', {'blog_post': blog_post})
