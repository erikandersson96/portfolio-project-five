from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


@login_required
def add_post(request):
    """
    A view for render add blog post &
    logic for add blog post
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
            messages.error(
                request, 'Failed to add the new blog post. \
                    Please ensure the form is valid.')
    else:
        post_form = PostForm()

    return render(request, template, context)


@login_required
def edit_post(request, slug):
    """
    A view for render edit blog post &
    logic for edit a post
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store managers can edit blog posts!')
        return redirect(reverse('home'))

    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, 'Successfully updated the post!')
            return redirect('blog')
        else:
            messages.error(request, 'Failed to update the post. \
                Please ensure the form is valid.')
    else:
        post_form = PostForm(instance=post)
        messages.info(
            request, f'You are currently editing: {post.slug}')

    template = 'blog/edit_blog_post.html'
    context = {
        'post_form': post_form,
        'post': post,
    }

    return render(request, template, context)
