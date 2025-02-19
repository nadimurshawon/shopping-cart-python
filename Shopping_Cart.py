# #Progect
        
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name}-${self.price}-{self.stock}"


# Create Customer
class Customer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class CartItem:
    def __init__(self, product, quantity):  # Corrected spelling of quantity
        self.product = product
        self.quantity = quantity  # Corrected spelling of quantity

    def get_total_price(self):
        return self.product.price * self.quantity  # Corrected to use self.quantity


class Cart:
    def __init__(self, customer):
        self.customer = customer
        self.cart = []  # Fixed the typo "car" to "cart"

    def add_to_cart(self, product, quantity):
        self.cart.append(CartItem(product, quantity))  # Fixed typo "CarTrem" to "CartItem"

    def calculate_total(self):
        total_price = 0
        for item in self.cart:
            total_price += item.get_total_price()  # Fixed missing accumulation of total_price
        return total_price

    def display_cart(self):
        print(f"Shopping Cart of {self.customer}")  # Fixed typo "Pself" to "self"

        for item in self.cart:
            print(f"{item.product.name} x {item.quantity} -$ {item.get_total_price()}")

        print(f"Total: $ {self.calculate_total()}")  # Fixed missing parentheses for method call


# Example usage
laptop = Product("laptop", 10000, 10)
phone = Product("IPhone", 20000, 20)

customer_name=input("Please Your Name__?")
shawon = Customer(customer_name)


shawon_cart = Cart(shawon)

shawon_cart.add_to_cart(laptop, 2)
shawon_cart.add_to_cart(phone, 1)

shawon_cart.display_cart()
