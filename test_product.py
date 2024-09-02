import pytest
from products import NonStockedProduct, LimitedProduct, Product, SecondHalfPrice, ThirdOneFree, PercentDiscount


def test_create_product():
    """Test that creating a standard product works."""
    product = Product(name="MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.get_quantity() == 100
    assert product.is_active() is True


def test_create_product_with_invalid_details():
    """Test that creating a product with invalid details raises an exception."""
    with pytest.raises(ValueError, match="Name cannot be empty."):
        Product("", price=1450, quantity=100)

    with pytest.raises(ValueError, match="Price cannot be negative."):
        Product("MacBook Air M2", price=-10, quantity=100)

    with pytest.raises(ValueError, match="Quantity cannot be negative."):
        Product("MacBook Air M2", price=1450, quantity=-5)


def test_product_inactivity():
    """Test that a product becomes inactive when quantity reaches zero."""
    product = Product(name="MacBook Air M2", price=1450, quantity=1)
    product.buy(1)
    assert product.is_active() is False


def test_product_purchase():
    """Test that purchasing a product updates the quantity and returns the correct price."""
    product = Product(name="MacBook Air M2", price=1450, quantity=10)
    total_price = product.buy(3)
    assert total_price == 1450 * 3
    assert product.get_quantity() == 7


def test_buying_more_than_available():
    """Test that attempting to buy more than the available quantity raises an exception."""
    product = Product(name="MacBook Air M2", price=1450, quantity=2)
    with pytest.raises(ValueError, match="Not enough quantity available for purchase."):
        product.buy(3)


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


def test_product_with_promotions():
    """Test that promotions are applied correctly to products."""
    product = Product(name="MacBook Air M2", price=1450, quantity=10)

    # Test No Promotion
    total_price = product.buy(1)
    assert total_price == 1450 * 1
    assert product.get_quantity() == 9

    # Test Second Half Price Promotion
    half_price_promo = SecondHalfPrice(name="Second Half price!")
    product.set_promotion(half_price_promo)
    total_price = product.buy(4)  # 2 at full price, 2 at half price
    assert total_price == 1450 * 2 + 1450 * 0.5 * 2
    assert product.get_quantity() == 5

    # Test Third One Free Promotion
    third_one_free_promo = ThirdOneFree(name="Third One Free!")
    product.set_promotion(third_one_free_promo)
    total_price = product.buy(3)  # 2 paid, 1 free
    assert total_price == 1450 * 2
    assert product.get_quantity() == 2

    # Test Percent Discount Promotion
    percent_discount_promo = PercentDiscount(name="30% off!", percent=30)
    product.set_promotion(percent_discount_promo)
    total_price = product.buy(2)  # 30% discount
    assert total_price == (1450 * 2) * (1 - 0.30)
    assert product.get_quantity() == 0
