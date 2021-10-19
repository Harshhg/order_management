

# We should use Django Dynamic Fixtures to create model objects, but for now creating it directly.
from order_management.products.models import Product


def create_product():
    return Product.objects.create(name="test_product", description="test product", price=100)


def create_product(**kwargs):
    name = kwargs.pop("name", "test-product")
    description = kwargs.pop("description", "test product")
    price = kwargs.pop("price", 100)
    return Product.objects.create(name=name, description=description, price=price, **kwargs)
