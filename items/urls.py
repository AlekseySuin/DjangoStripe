from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:id>/', views.buy_item, name='buy_item'),
    path('items/<int:id>/', views.item_detail, name='item_detail'),
    path('orders/<int:id>/checkout/', views.order_checkout_session, name='order_checkout'),
    path('orders/<int:id>/', views.order_detail, name='order_details'),
]