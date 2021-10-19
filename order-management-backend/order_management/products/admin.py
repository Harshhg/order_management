from django.contrib import admin

from order_management.products.models import Product


@admin.register(Product)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "price"]
    fields = [
        "name",
        "description",
        "price",
    ]
