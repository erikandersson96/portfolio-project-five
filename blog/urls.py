from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_posts, name='blog'),
    path('add_post/', views.add_post, name='add_post'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
]
