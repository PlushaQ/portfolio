from django.urls import path, include

from . import views

urlpatterns = [
               path("", views.all_posts, name="all_posts"),
               path('post-<int:blog_id>/', views.blog_post, name='blog_post')
              ]
