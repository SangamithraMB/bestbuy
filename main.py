from products import Product, NonStockedProduct, LimitedProduct, SecondHalfPrice, ThirdOneFree, PercentDiscount
from store import Store

product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
    NonStockedProduct("Windows License", price=125),
    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

second_half_price = SecondHalfPrice("Second Half price!")
third_one_free = ThirdOneFree("Third One Free!")
thirty_percent = PercentDiscount("30% off!", percent=30)

product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)


best_buy = Store(product_list)


def print_store_menu():
    """
        Prints the store menu with options for the user to select.
    """
    store_menu = """   
    Store Menu
    ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
    """
    print(store_menu)


def listing_all_products(store: Store):
    """
        Lists all products in the store with their respective details.

        Args:
            store (Store): The store object containing products.

        Returns:
            str: A string listing all products with their details.
    """
    product_info = []
    for ids, product in enumerate(store.get_all_products(), start=1):
        product_info.append(f"{ids}. {product.show()}")
    return "\n".join(product_info)


def show_total_amount(store: Store):
    """
        Displays the total quantity of all products available in the store.

        Args:
            store (Store): The store object containing products.
    """
    total_quantity = store.get_total_quantity()
    print(f"Total of {total_quantity} items in store")


def make_order(store: Store):
    """
        Allows the user to make an order by selecting products and quantities.
        Displays the total price after the order is completed.

        Args:
            store (Store): The store object containing products.
    """
    enumerated_product = [(index, product) for index, product in
                          enumerate(store.get_all_products(), start=1)]
    print("------")
    for ids, product in enumerated_product:
        print(f"{ids}. {product.show()}")
    print("------")
    print("When you want to finish order, enter empty text.")
    shopping_list = []
    while True:
        product_choice = input("Which product # do you want? ").strip()
        quantity = input("What amount do you want? ").strip()
        if product_choice == '' or quantity == '':
            break
        else:
            try:
                product_choice = int(product_choice)
                quantity = int(quantity)
                if 0 < product_choice <= len(enumerated_product):
                    selected_product = enumerated_product[product_choice - 1][1]
                    shopping_list.append((selected_product, quantity))
                    print("Product added to list!\n")
                else:
                    print("Error adding product!")
            except ValueError:
                print("Error adding product!")

    if shopping_list:
        try:
            total_price = store.order(shopping_list)
            print(f"\nOrder made! Total payment: ${round(total_price, 2)} ")
        except ValueError as e:
            print(f"Order error: {e}")


def start(store: Store):
    """
        Starts the main loop of the store application, allowing the user to interact with the store menu.

        Args:
            store (Store): The store object containing products.
    """
    while True:
        try:
            print_store_menu()
            user_choice = int(input("Please choose a number: "))
            if user_choice == 1:
                print("------")
                print(listing_all_products(store))
                print("------")
            elif user_choice == 2:
                show_total_amount(store)
            elif user_choice == 3:
                make_order(store)
            elif user_choice == 4:
                break
            else:
                continue
        except ValueError:
            print("Error with your choice! Try again!")


if __name__ == "__main__":
    start(best_buy)
