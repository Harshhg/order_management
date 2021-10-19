from rest_framework import serializers

from order_management.orders.models import Order
from order_management.products.models import Product
from order_management.products.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Order
        fields = ["id", "created_at", "amount", "product"]


class OrderCreateSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField()
