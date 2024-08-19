class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class POS:
    def __init__(self):
        self.products = {}
        self.cart = []

    def add_product(self, name, price, stock):
        if name in self.products:
            print("Product already exists. Updating stock.")
            self.products[name].stock += stock
        else:
            self.products[name] = Product(name, price, stock)
        print(f"Product {name} added/updated.")

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print(f"Product {name} removed.")
        else:
            print("Product not found.")

    def view_products(self):
        if not self.products:
            print("No products available.")
        else:
            print("\nAvailable Products:")
            for product in self.products.values():
                print(f"Name: {product.name}, Price: {product.price}, Stock: {product.stock}")

    def add_to_cart(self, name, quantity):
        if name in self.products:
            product = self.products[name]
            if product.stock >= quantity:
                self.cart.append((product, quantity))
                product.stock -= quantity
                print(f"{quantity} units of {name} added to cart.")
            else:
                print(f"Insufficient stock for {name}.")
        else:
            print("Product not found.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("\nItems in Cart:")
            for item, quantity in self.cart:
                print(f"Product: {item.name}, Quantity: {quantity}, Total Price: {item.price * quantity}")

    def checkout(self):
        if not self.cart:
            print("Your cart is empty.")
            return

        total = sum(item.price * quantity for item, quantity in self.cart)
        print("\nCheckout:")
        self.view_cart()
        print(f"Total Amount: {total}")

        payment = float(input("Enter payment amount: "))
        if payment >= total:
            change = payment - total
            print(f"Payment successful! Change: {change}")
            self.cart.clear()
        else:
            print("Insufficient payment. Please try again.")

def main():
    pos_system = POS()

    while True:
        print("\nOptions:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Products")
        print("4. Add to Cart")
        print("5. View Cart")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '7':
            print("Exiting POS system.")
            break

        if choice == '1':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            pos_system.add_product(name, price, stock)

        elif choice == '2':
            name = input("Enter product name to remove: ")
            pos_system.remove_product(name)

        elif choice == '3':
            pos_system.view_products()

        elif choice == '4':
            name = input("Enter product name: ")
            quantity = int(input(f"Enter quantity of {name}: "))
            pos_system.add_to_cart(name, quantity)

        elif choice == '5':
            pos_system.view_cart()

        elif choice == '6':
            pos_system.checkout()

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
