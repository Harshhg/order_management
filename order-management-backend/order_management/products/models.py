from django.db import models

from order_management.base.models import TimeStampedUUIDModel


class Product(TimeStampedUUIDModel):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
