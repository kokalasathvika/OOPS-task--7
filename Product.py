class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_price_tag(self):
        print(f"Product: {self.name}")
        print(f"Price: ₹{self.price}")


# Taking input
name = input("Product Name: ")
price = input("Price: ")

# Creating object
product = Product(name, price)

# Printing formatted price tag
product.print_price_tag()