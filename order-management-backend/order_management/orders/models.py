# from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

from order_management.base.models import TimeStampedUUIDModel
from order_management.products.models import Product


class Order(TimeStampedUUIDModel):
    amount = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders")