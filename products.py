from abc import ABC, abstractmethod


class Product:
    """
       A class representing a product in a store.

       Attributes:
           name (str): The name of the product.
           price (float): The price of the product.
           _quantity (int): The quantity of the product in stock.
           active (bool): The status of the product, whether it is active or not.

       Methods:
           get_quantity() -> float: Returns the current quantity of the product.
           set_quantity(quantity): Sets the product's quantity and deactivates it if the quantity is zero.
           is_active() -> bool: Returns the active status of the product.
           activate(): Activates the product.
           deactivate(): Deactivates the product.
           show() -> str: Returns a string representation of the product's details.
           buy(quantity) -> float: Processes a purchase of the product,
           reducing its quantity and returning the total price.
    """

    def __init__(self, name, price, quantity):
        """
                Initializes a new Product instance.

                Args:
                    name (str): The name of the product. Must not be empty.
                    price (float): The price of the product. Must not be negative.
                    quantity (int): The initial quantity of the product. Must not be negative.

                Raises:
                    ValueError: If name is empty, or if price or quantity are negative.
        """
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self._quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self) -> float:
        """
                Returns the current quantity of the product.

                Returns:
                    float: The quantity of the product.
        """
        return self._quantity

    def set_quantity(self, quantity):
        """
                Sets the quantity of the product. Deactivates the product if the quantity is zero.

                Args:
                    quantity (int): The new quantity of the product. Must not be negative.

                Raises:
                    ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
                Checks if the product is active.

                Returns:
                    bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def set_promotion(self, promotion: 'Promotion'):
        if promotion is not None and not isinstance(promotion, Promotion):
            raise ValueError("Promotion must be an instance of the Promotion class.")
        self.promotion = promotion

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self._quantity:
            raise ValueError("Not enough quantity available for purchase.")

        total_price = quantity * self.price
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)

        new_quantity = self._quantity - quantity
        self.set_quantity(new_quantity)
        return total_price

    def show(self) -> str:
        """
                Returns a string representation of the product's details.

                Returns:
                    str: A string showing the product's name, price, and quantity.
        """
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: ${self.price:.2f}, Quantity: {self._quantity}{promotion_info}"


class NonStockedProduct(Product):
    """
    Represents a product that is not physically stocked in the store.
    """

    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        if quantity != 0:
            raise ValueError("Non-stocked products cannot have a quantity other than 0.")
        # Quantity is always 0 for NonStockedProduct
        super().set_quantity(quantity)


class LimitedProduct(Product):
    """
    Represents a product that has a maximum purchase limit per order.
    """

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("Maximum purchase quantity must be greater than zero.")
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} of '{self.name}' at once.")
        return super().buy(quantity)


# Promotion Classes

class Promotion(ABC):
    """
    Abstract base class for promotions.
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: 'Product', quantity) -> float:
        pass


class SecondHalfPrice(Promotion):
    """
        Promotion where every second item is at half price.
    """
    def apply_promotion(self, product: 'Product', quantity) -> float:
        if quantity <= 1:
            return product.price * quantity

        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items

        total_price = (full_price_items * product.price) + (half_price_items * product.price * 0.5)
        return total_price


class ThirdOneFree(Promotion):
    """
        Promotion where you get one free item for every two purchased.
    """
    def apply_promotion(self, product: 'Product', quantity) -> float:
        if quantity <= 2:
            return product.price * quantity

        free_items = quantity // 3
        paid_items = quantity - free_items

        total_price = paid_items * product.price
        return total_price


class PercentDiscount(Promotion):
    """
        Promotion that applies a percentage discount.
    """
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        if not (0 < percent < 100):
            raise ValueError("Percent must be between 0 and 100.")
        self.percent = percent

    def apply_promotion(self, product: 'Product', quantity) -> float:
        return (product.price * quantity) * (1 - self.percent / 100)


if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())
