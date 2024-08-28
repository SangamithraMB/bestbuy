class Product:
    def __init__(self, name, price, quantity):
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
        return self._quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity Cannot be zero or negative.")
        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self._quantity}"

    def buy(self, quantity) -> float:
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
