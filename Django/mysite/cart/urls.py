from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_request, name='category-list'),
    path('categories/<int:category_id>/', views.category_request, name='category-detail'),
    path('products/', views.product_request, name='product-list'),
    path('products/<int:product_id>/', views.product_request, name='product-detail'),
    path('cart-items/', views.cart_item_request, name='cart-item-list'),
    path('cart-items/<int:cart_item_id>/', views.cart_item_request, name='cart-item-detail'),
]
