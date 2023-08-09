import json
from django.shortcuts import get_object_or_404, render
from .models import Category, Product, Cart, CartItem
from django.db.models import F
from django.http import JsonResponse
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt

def index(request):
    products = Product.objects.filter(on_sale=True)

    context = {
        'products': products
    }

    return render(request, 'index.html', context)

def all_product(request):
    products = Product.objects.annotate(on_sale_last=F('on_sale')).order_by('-on_sale_last', '-id')

    context = {
        'products': products
    }

    return render(request, 'all_product.html', context)

def product_detail(request, product_slug):
    # Slug değerine göre ürünü veritabanından getir
    product = get_object_or_404(Product, slug=product_slug)
    
    # Aynı kategorilere sahip satışta olan ürünleri getir, mevcut ürünü hariç tut ve 5 tanesini rastgele seç
    related_products = Product.objects.filter(categories__in=product.categories.all(), on_sale=True).exclude(id=product.id).distinct().order_by('?')[:4]


    context = {
        'product': product,
        'related_products': related_products
    }

    return render(request, 'product_detail.html', context)

def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.products.filter(on_sale=True)

    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'category_detail.html', context)

from django.db.utils import IntegrityError

@csrf_exempt
def add_to_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        product = Product.objects.get(id=product_id)

        # Ürünün aktif olup olmadığını kontrol et
        if not product.on_sale:  # Eğer üründe on_sale adında bir alan yoksa, bu kontrolü uygun bir şekilde değiştirin.
            return JsonResponse({"message": "This product is currently inactive."})

        # Örnek olarak varsayılan bir sepeti alıyoruz.
        cart = Cart.objects.first()

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += int(quantity)
        else:
            cart_item.quantity = int(quantity)
        cart_item.save()

        return JsonResponse({"message": "Product successfully added to the cart"})

    
def update_quantity(request, item_id, action):
    try:
        cart_item = CartItem.objects.get(id=item_id)
        if action == 'increase':
            cart_item.quantity += 1
        elif action == 'decrease':
            cart_item.quantity -= 1
            if cart_item.quantity <= 0:
                cart_item.delete()
                return JsonResponse({'success': True})
        cart_item.save()
        return JsonResponse({'success': True})
    except CartItem.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'CartItem not found!'})

def remove_from_cart(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.delete()
        return JsonResponse({'success': True})
    except CartItem.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'CartItem not found!'})