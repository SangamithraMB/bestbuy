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
           buy(quantity) -> float: Processes a purchase of the product, reducing its quantity and returning the total price.
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
            raise ValueError("Quantity Cannot be zero or negative.")
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
        """
                Activates the product, making it available for purchase.
        """
        self.active = True

    def deactivate(self):
        """
                Deactivates the product, making it unavailable for purchase.
        """
        self.active = False

    def show(self) -> str:
        """
                Returns a string representation of the product's details.

                Returns:
                    str: A string showing the product's name, price, and quantity.
        """
        return f"{self.name}, Price: ${self.price}, Quantity: {self._quantity}"

    def buy(self, quantity) -> float:
        """
                Processes a purchase of the product.

                Args:
                    quantity (int): The amount of product to buy. Must be greater than zero and less than or equal to the available quantity.

                Returns:
                    float: The total price for the quantity of product bought.

                Raises:
                    ValueError: If quantity is less than or equal to zero, or if there isn't enough quantity available.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self._quantity:
            raise ValueError("Not enough quantity available for purchase.")
        total_price = quantity * self.price
        self.set_quantity(self._quantity - quantity)
        return total_price


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
