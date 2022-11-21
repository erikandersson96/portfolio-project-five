from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import BlogPost, BlogComment
from .forms import PostForm, CommentForm


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
def add_post(request, ):
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


@login_required
def delete_post(request, slug):
    """
    A view for store managers to delete blog posts
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store managers can delete blog posts!')
        return redirect(reverse('home'))

    blog_post = get_object_or_404(BlogPost, slug=slug)
    blog_post.delete()
    messages.success(request, 'The blog post was deleted!')
    return redirect(reverse('blog'))


class AddCommentView(CreateView):
    """
    A view for Create comments on blog posts
    """
    model = BlogComment
    form_class = CommentForm
    template_name = 'comments/add_comment.html'

    def form_valid(self, form):
        form.instance.post = BlogPost.objects.get(slug=self.kwargs.get('slug'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        blog_post = BlogPost.objects.get(slug=self.kwargs.get('slug'))
        data = super().get_context_data(**kwargs)
        data['blog_post'] = blog_post
        return data

    def get_success_url(self):
        return reverse_lazy(
            'blog_detail', kwargs={'slug': self.kwargs.get('slug')})


def delete_comment(request, comment_id):
    """
    View for delete blog post comments
    """
    comment = get_object_or_404(BlogComment, pk=comment_id)
    comment.delete()
    messages.success(request, 'The blog comment was deleted!')
    return redirect(reverse('blog'))
