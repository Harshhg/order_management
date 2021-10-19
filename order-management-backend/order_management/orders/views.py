from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from order_management.orders.models import Order
from order_management.orders.serializers import OrderSerializer, OrderCreateSerializer
from order_management.orders.services import create_order, update_order


class OrderViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    response_serializer = OrderSerializer

    serializer_classes = {
        "list": OrderSerializer,
        "create": OrderCreateSerializer,
        "update": OrderCreateSerializer
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in self.serializer_classes:
            return self.serializer_classes[self.action]
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.validated_data.get("product")
        quantity = serializer.validated_data.get("quantity")
        order = create_order(request.user, product, quantity)
        response_serializer = self.response_serializer(order)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        serializer = self.get_serializer_class()(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        order = update_order(order, **serializer.validated_data)
        response_serializer = self.response_serializer(order)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


