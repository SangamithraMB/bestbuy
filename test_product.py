import pytest
from products import Product


def test_create_normal_product():
    """Test that creating a normal product works."""
    product = Product(name="MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.get_quantity() == 100
    assert product.is_active() is True


def test_create_product_with_empty_name():
    """Test that creating a product with an empty name raises a ValueError."""
    with pytest.raises(ValueError, match="Name cannot be empty."):
        Product(name="", price=1450, quantity=100)


def test_create_product_with_negative_price():
    """Test that creating a product with a negative price raises a ValueError."""
    with pytest.raises(ValueError, match="Price cannot be negative."):
        Product(name="MacBook Air M2", price=-10, quantity=100)


def test_create_product_with_negative_quantity():
    """Test that creating a product with a negative quantity raises a ValueError."""
    with pytest.raises(ValueError, match="Quantity cannot be negative."):
        Product(name="MacBook Air M2", price=1450, quantity=-10)


def test_product_becomes_inactive_when_quantity_zero():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    product = Product(name="MacBook Air M2", price=1450, quantity=10)
    product.set_quantity(0)
    assert product.is_active() is False


def test_product_purchase_modifies_quantity_and_returns_right_output():
    """Test that product purchase modifies the quantity and returns the correct total price."""
    product = Product(name="MacBook Air M2", price=1450, quantity=10)
    total_price = product.buy(2)
    assert product.get_quantity() == 8
    assert total_price == 2 * 1450


def test_buying_more_than_available_quantity_raises_exception():
    """Test that buying a larger quantity than exists raises a ValueError."""
    product = Product(name="MacBook Air M2", price=1450, quantity=10)
    with pytest.raises(ValueError, match="Not enough quantity available for purchase."):
        product.buy(15)
