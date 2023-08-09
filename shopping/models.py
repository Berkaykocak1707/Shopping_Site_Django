from django.db import models
from autoslug import AutoSlugField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
import random
import os

def image_upload_path(instance, filename):
    """Generate file path for uploaded images with slug name"""
    ext = filename.split('.')[-1]
    return os.path.join('products/', f"{instance.slug}.{ext}")

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=image_upload_path)
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFill(100, 100)],
                               format='JPEG',
                               options={'quality': 60})
    slug = AutoSlugField(populate_from='name', unique=True, blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='products')
    special_code = models.CharField(max_length=100, unique=True, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    on_sale = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # If special_code is not provided, generate one
        if not self.special_code:
            initials = ''.join([word[0] for word in self.name.split() if word]).upper()
            random_number = random.randint(10000, 99999)
            self.special_code = f"{initials}-{random_number}"

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Cart(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Cart {self.id}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.subtotal = self.product.price * self.quantity
        super(CartItem, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
