from django.contrib import admin
from .models import Product, Category, Cart, CartItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'old_price', 'on_sale', 'special_code']
    list_filter = ['on_sale', 'categories']
    search_fields = ['name', 'special_code']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id']  # Sepet modelinizde başka alanlar da varsa bu listeye ekleyebilirsiniz.

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'subtotal']
