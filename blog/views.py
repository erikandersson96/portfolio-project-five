from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
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


def blog_detail(request, slug):
    """
    A view for render blog post detail page
    """
    blog_post_detail = get_object_or_404(BlogPost, slug=slug)

    context = {
        'blog_post_detail': blog_post_detail,
    }

    return render(request, 'blog/blog_detail.html', context)


def add_post(request):
    """
    A view for render all blog posts page,
    to add blog posts by admin/store owner
    """

    template = 'blog/add_blog_post.html'

    return render(request, template)
