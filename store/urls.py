from django.urls import path
from .views import (
    home_view, product_single_view, category_view,
    cart_view, cart_add_view, checkout_view,
    cart_delete_view,
)

urlpatterns = [
    path('', home_view),
    path('product/<int:pk>/', product_single_view),
    path('categories/', category_view),
    path('cart/', cart_view),
    path('cart/add/', cart_add_view),
    path('cart/delete/', cart_delete_view),
    path('checkout/', checkout_view),
]
