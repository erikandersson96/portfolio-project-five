from django.contrib import admin
from .models import BlogPost, BlogComment


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """ Register admin for blog posts """

    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on',)


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    """ Register admin for blog comments """

    list_display = ('name', 'body', 'post', 'created_on',)
    list_filter = ('created_on',)
    search_fields = ('name', 'body')
