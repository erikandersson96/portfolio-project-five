from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import BlogPost
from .forms import PostForm


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
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store managers can add blog posts!')
        return redirect(reverse('home'))

    template = 'blog/add_blog_post.html'

    post_form = PostForm(request.POST or None, request.FILES or None)

    context = {
        'post_form': post_form,
    }

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form = post_form.save(commit=False)
            post_form.author = request.user
            post_form.status = 1
            post_form.save()
            messages.success(
                request, 'You have successfully added the new blog post!')
            return redirect('blog')
        else:
            print(post_form.errors)
            # messages.error(
            #     request, 'Failed to add the new blog post. \
            #         Please ensure the form is valid.')
    else:
        post_form = PostForm()

    return render(request, template, context)
