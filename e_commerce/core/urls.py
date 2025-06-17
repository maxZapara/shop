from django.contrib import admin
from django.urls import path
from .views import home,product_details, delete_comment, cart, product_list

urlpatterns = [
    path('',home, name='home'),
    path("products", product_list, name='product_list'),
    path('product/details/<id>',product_details, name='product_details'),
    path('cart', cart, name="cart"),
    path('comments/<comment_id>/delete', delete_comment, name='delete_comment'),

]   