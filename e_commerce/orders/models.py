from django.db import models
from core.models import Product

# Create your models here.

class Order(models.Model):
    STATUS_CHOISES=[
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("shipped", "Shipped"),
        ("derivered", "Derivered"),
        ("cancelled", "Canselled"),
    ]

    first_name=models.CharField(max_length=50, null=False, blank=False)
    last_name=models.CharField(max_length=50, null=False, blank=False)
    adress=models.CharField(max_length=255, null=False, blank=False)
    city=models.CharField(max_length=100, null=False, blank=False)
    state=models.CharField(max_length=100, null=False, blank=False)
    postal_code=models.CharField(max_length=20, null=False, blank=False)
    order_notes=models.TextField(null=True, blank=True)
    total_price=models.DecimalField(max_digits=40, decimal_places=2, default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=50, choices=STATUS_CHOISES, default="pending")

    def calculate_total_price(self):
        total=sum(
            item.product.price*item.quantity for item in self.items)
        self.total_price=total
        self.save()

    def __str__(self):
        return f"Order by:{self.first_name} {self.last_name} with status: {self.status}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

