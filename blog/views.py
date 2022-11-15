from django.shortcuts import render
from .models import BlogPost


def all_posts(request):
    """
    A view for render all blog posts page
    """
    all_blog_posts = BlogPost.objects.all()

    context = {
        'all_blog_posts': all_blog_posts,
    }

    return render(request, 'blog/blog.html', context)
