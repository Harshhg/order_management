from order_management.orders.models import Order


def get_total_amount(quantity, product_price):
    return product_price * quantity


def create_order(user, product, quantity):
    return Order.objects.create(
        amount=get_total_amount(quantity, product.price),
        quantity=quantity,
        user=user,
        product=product
    )


def update_order(order, **kwargs):
    quantity = kwargs.get("quantity", 1)
    order.quantity = quantity
    order.amount = get_total_amount(quantity, order.product.price)
    order.save()
    return order