from datetime import datetime

class Product:
    def __init__(self, product_id, name, category, quantity, price_per_unit, expiry_month=None, expiry_year=None):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.expiry_month = expiry_month
        self.expiry_year = expiry_year

    def display_product_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Quantity: {self.quantity}")
        print(f"Price Per Unit: {self.price_per_unit}")
        if self.expiry_month and self.expiry_year:
            print(f"Expiry Date: {self.expiry_month}/{self.expiry_year}")
        else:
            print("Expiry Date: N/A")


class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product):
        self.inventory[product.product_id] = product

    def remove_product(self, product_id):
        if product_id in self.inventory:
            del self.inventory[product_id]
        else:
            print("Product not found in inventory.")

    def update_quantity(self, product_id, new_quantity):
        if product_id in self.inventory:
            self.inventory[product_id].quantity = new_quantity
        else:
            print("Product not found in inventory.")

    def update_price(self, product_id, new_price):
        if product_id in self.inventory:
            self.inventory[product_id].price_per_unit = new_price
        else:
            print("Product not found in inventory.")

    def search_product(self, search_term):
        found = False
        for product_id, product in self.inventory.items():
            if search_term.lower() in product.name.lower():
                found = True
                print("Product Found:")
                product.display_product_info()
                print()

        if not found:
            print("Product not found in inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for product_id, product in self.inventory.items():
            print(f"Product ID: {product_id}")
            product.display_product_info()
            print()


def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Quantity")
        print("4. Update Price")
        print("5. Search Product by ID or Name")
        print("6. Display Inventory")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            category = input("Enter Product Category: ")
            quantity = int(input("Enter Quantity: "))
            price_per_unit = float(input("Enter Price Per Unit: "))
            expiry_month = int(input("Enter Expiry Month (MM), if applicable, else press enter: "))
            expiry_year = int(input("Enter Expiry Year (YYYY), if applicable, else press enter: "))

            product = Product(product_id, name, category, quantity, price_per_unit, expiry_month, expiry_year)
            inventory.add_product(product)
        elif choice == '2':
            product_id = input("Enter Product ID: ")
            inventory.remove_product(product_id)
        elif choice == '3':
            product_id = input("Enter Product ID: ")
            new_quantity = int(input("Enter new quantity: "))
            inventory.update_quantity(product_id, new_quantity)
        elif choice == '4':
            product_id = input("Enter Product ID: ")
            new_price = float(input("Enter new price per unit: "))
            inventory.update_price(product_id, new_price)
        elif choice == '5':
            search_term = input("Enter Product ID or Name to search: ")
            inventory.search_product(search_term)
        elif choice == '6':
            inventory.display_inventory()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
