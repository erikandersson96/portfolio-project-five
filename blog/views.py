from django.shortcuts import render
from .models import BlogPost


def all_posts(request):
    """
    A view for render all blog posts page
    """
    blog = BlogPost.objects.all()

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog.html', context)
