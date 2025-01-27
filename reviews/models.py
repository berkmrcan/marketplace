from django.db import models
from products.models import Product
from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        unique_together = ("product", "user")


    def save(self, *args, **kwargs):
        """Override save method to update product ratings after saving."""
        super().save(*args, **kwargs)
        self.product.update_reviews_summary()

    def delete(self, *args, **kwargs):
        """Override delete method to update product ratings after deletion."""
        product = self.product 
        super().delete(*args, **kwargs)
        product.update_reviews_summary()
