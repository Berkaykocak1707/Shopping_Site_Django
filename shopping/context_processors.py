# context_processors.py

from .models import Category, Cart, CartItem


def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def cart_context(request):
    # Örnek olarak varsayılan bir sepeti alıyoruz.
    # Gerçek bir uygulamada, oturum (session) ya da cookie bilgisine göre kullanıcının sepetini alabilirsiniz.
    cart = Cart.objects.first()
    
    # Bu sepete ait ürünleri alıyoruz.
    cart_items = CartItem.objects.filter(cart=cart)
    # Toplam ürün adedini hesapla
    total_quantity = sum([item.quantity for item in cart_items])

    return {'cart_items': cart_items, 'total_quantity': total_quantity}