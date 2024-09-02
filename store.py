from typing import List, Tuple

from products import Product


class Store:
    """
        A class representing a store that manages a collection of products.

        Attributes:
            products (List[Product]): A list of products available in the store.

        Methods:
            add_product(product: Product): Adds a product to the store's inventory.
            remove_product(product: Product): Removes a product from the store's inventory.
            get_total_quantity() -> int: Returns the total quantity of all products in the store.
            get_all_products() -> List[Product]: Returns a list of all active products in the store.
            order(shopping_list: List[Tuple[Product, int]]) -> float:Processes an order from store & returns total price
    """
    def __init__(self, initial_products: List[Product]):
        """
                Initializes the Store with a list of products.

                Args:
                    initial_products (List[Product]): A list of products to be added to the store's inventory.
        """
        self.products = initial_products

    def add_product(self, product: Product):
        """
                Adds a product to the store's inventory.

                Args:
                    product (Product): The product to be added.
        """
        self.products.append(product)

    def remove_product(self, product: Product):
        """
                Removes a product from the store's inventory.

                Args:
                    product (Product): The product to be removed.
        """
        self.products = [item for item in self.products if item != product]

    def get_total_quantity(self) -> int:
        """
                Calculates the total quantity of all products in the store.

                Returns:
                    int: The total quantity of all products.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """
                Retrieves a list of all active products in the store.

                Returns:
                    List[Product]: A list of active products.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
            Processes an order, purchasing the specified quantities of products.

            Args:
                shopping_list (List[Tuple[Product, int]]): A list of tuples where each tuple contains a product and
                the quantity to purchase.

            Returns:
                float: The total price of the order.

            Raises:
                ValueError: If a product in the order is not active or if the purchase cannot be completed.
        """
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
