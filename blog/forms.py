from django import forms
from .models import BlogPost, BlogComment


class PostForm(forms.ModelForm):
    """
    Form for adding a blog post
    """
    class Meta:
        model = BlogPost
        fields = [
            'slug',
            'title',
            'author',
            'content',
            'image',
        ]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    """
    Form for adding comment on a post
    """
    class Meta:
        model = BlogComment
        fields = [
            'name',
            'body',
        ]
