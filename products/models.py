from django.db import models
from django.db.models import Avg, Count, CheckConstraint, Q
from users.models import CustomUser

class Product(models.Model):
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    inventory = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    average_rating = models.FloatField(default=0.0)
    total_reviews = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(price__gte=0.01) & Q(inventory__gte=0),
                name="valid_price_and_inventory",
            ),
        ]


    def __str__(self):
        return self.name

    def update_reviews_summary(self):
        """Recalculates and updates the average rating and total reviews."""
        review_summary = self.reviews.aggregate(
            avg_rating=Avg('rating'),
            total=Count('id')
        )
        self.average_rating = review_summary['avg_rating'] or 0.0
        self.total_reviews = review_summary['total']
        self.save()
