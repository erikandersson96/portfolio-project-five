from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('wish_list/', views.all_favourites, name='wish_list'),
    path('order_history/<order_number>', views.order_history,
         name='order_history'),
]
