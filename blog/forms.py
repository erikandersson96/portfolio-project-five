from django import forms
from .models import BlogPost


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
