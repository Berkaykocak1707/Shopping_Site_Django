from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shopping-index'),
    path('all-product/', views.all_product, name='all-product'),
    path('product/<slug:product_slug>/', views.product_detail, name='product-detail'),
    path('category/<slug:category_slug>/', views.category_detail, name='category-detail'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('update-quantity/<int:item_id>/<str:action>/', views.update_quantity, name='update_quantity'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]