from decimal import Decimal

from django.urls import reverse
from rest_framework.test import APITestCase

from order_management.orders.models import Order
from order_management.products.tests.factories import create_product
from order_management.users.tests.factories import create_user


class OrderCreateTestCases(APITestCase):
    def setUp(self):
        super().setUp()
        self.quantity = 5
        self.product_price = 1000
        self.total_amount = self.quantity * self.product_price

        self.product = create_product(price=self.product_price)
        self.user = create_user()

        self.request_body = {
            "product": str(self.product.id),
            "quantity": self.quantity
        }
        self.response_keys = {
            "id",
            "product",
            "amount",
            "created_at"
        }
        self.url = reverse("orders-list")

    def test_user_order(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_user_create_order(self):
        self.client.force_authenticate(self.user)
        response = self.client.post(self.url, data=self.request_body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(set(response.data), self.response_keys)
        self.assertEqual(Decimal(response.data["amount"]), self.total_amount)
        self.assertEqual(Order.objects.count(), 1)

    def test_user_update_order(self):
        self.client.force_authenticate(self.user)
        # Create Order -
        response = self.client.post(self.url, data=self.request_body)
        self.assertEqual(response.status_code, 201)
        order_id = response.data["id"]

        # Update Order
        url = reverse("orders-detail", args=[str(order_id)])
        self.request_body.update({"quantity": 1})
        response = self.client.put(url, data=self.request_body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(set(response.data), self.response_keys)
        self.assertEqual(Decimal(response.data["amount"]), self.product_price)
        self.assertEqual(Order.objects.count(), 1)

    def test_user_delete_order(self):
        self.client.force_authenticate(self.user)
        # Create Order -
        response = self.client.post(self.url, data=self.request_body)
        self.assertEqual(response.status_code, 201)
        order_id = response.data["id"]

        # Delete Order
        url = reverse("orders-detail", args=[str(order_id)])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Order.objects.count(), 0)
