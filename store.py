from typing import List, Tuple

from products import Product


class Store:
    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        self.products = [item for item in self.products if item != product]

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            if not product.is_active():
                raise ValueError(f"Product '{product.name}' is not active and cannot be purchased.")
            total_price += product.buy(quantity)
        return total_price


if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    store = Store(product_list)

    products = store.get_all_products()

    print(store.get_total_quantity())

    price = store.order([(products[0], 2), (products[1], 2)])
    print(f"Order cost: {price} dollars.")