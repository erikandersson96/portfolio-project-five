from django.shortcuts import render
from .models import BlogPost


def post(request):
    """
    A view for render contact us page
    """

    return render(request, 'blog/blog.html')
