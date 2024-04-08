from django.urls import path, include
from . import views

app_name = 'shop'
urlpatterns = [
    # Профиль
    path('', views.index_page, name='index-page'),
    path('profile/', views.profile_page, name='profile-page'),
    path('profile/edit', views.edit_profile, name='edit-profile-page'),
    # Корзина
    path('cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('products/', views.view_products, name='view_products'),
    
    path('products/<int:product_id>', views.single_product, name='single_product'),
]