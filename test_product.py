import pytest
from products import NonStockedProduct, LimitedProduct


def test_create_non_stocked_product():
    """Test that creating a non-stocked product works."""
    product = NonStockedProduct(name="Windows License", price=125)
    assert product.name == "Windows License"
    assert product.price == 125
    assert product.get_quantity() == 0
    assert product.is_active() is True


def test_non_stocked_product_quantity_cannot_be_set():
    """Test that setting quantity of non-stocked product raises an exception."""
    product = NonStockedProduct(name="Windows License", price=125)
    with pytest.raises(ValueError, match="Non-stocked products cannot have a quantity other than 0."):
        product.set_quantity(10)


def test_create_limited_product():
    """Test that creating a limited product works."""
    product = LimitedProduct(name="Shipping", price=10, quantity=250, maximum=1)
    assert product.name == "Shipping"
    assert product.price == 10
    assert product.get_quantity() == 250
    assert product.maximum == 1


def test_limited_product_buy_within_limit():
    """Test that buying within the limit for a limited product works."""
    product = LimitedProduct(name="Shipping", price=10, quantity=250, maximum=1)
    total_price = product.buy(1)
    assert product.get_quantity() == 249
    assert total_price == 10


def test_limited_product_buy_exceeding_limit():
    """Test that buying more than the limit for a limited product raises an exception."""
    product = LimitedProduct(name="Shipping", price=10, quantity=250, maximum=1)
    with pytest.raises(ValueError, match="Cannot purchase more than 1 of 'Shipping' at once."):
        product.buy(2)
