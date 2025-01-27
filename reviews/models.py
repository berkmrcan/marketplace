from django.db import models
from products.models import Product
from users.models import CustomUser

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """Override save method to update product ratings after saving."""
        super().save(*args, **kwargs)
        self.product.update_reviews_summary()

    def delete(self, *args, **kwargs):
        """Override delete method to update product ratings after deletion."""
        product = self.product 
        super().delete(*args, **kwargs)
        product.update_reviews_summary()
