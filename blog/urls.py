from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_posts, name='blog'),
    path('add_post/', views.add_post, name='add_post'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('edit_post/<slug:slug>/', views.edit_post, name='edit_post'),
    path('<slug:slug>/comment', views.AddCommentView.as_view(),
         name='add_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment,
         name='delete_comment'),
    path('delete_post/<slug:slug>/', views.delete_post,
         name='delete_post'),
]
