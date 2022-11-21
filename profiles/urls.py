from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('wish_list/', views.AllFavourites.as_view(), name='wish_list'),
    path('add_favorite/<int:product_id>/', views.add_favorite_watch,
         name='add_favorite'),
    path('order_history/<order_number>', views.order_history,
         name='order_history'),
]
