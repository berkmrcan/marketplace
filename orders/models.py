from django.db import models
from products.models import Product
from users.models import CustomUser, ShippingAddress

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    buyer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.SET_NULL, null=True, blank=True)

    
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("shipped", "Shipped"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.product:
            self.total_price = self.amount * self.product.price
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Order {self.id} - {self.buyer} - {self.product} ({self.amount})"
