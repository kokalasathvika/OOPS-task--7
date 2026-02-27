class Customer:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def print_delivery_details(self):
        print("Delivery Details")
        print(f"Customer: {self.name}")
        print(f"Address: {self.address}")


# Input
name = input("Customer Name: ")
address = input("Address: ")

# Object creation
customer = Customer(name, address)

# Display delivery details
customer.print_delivery_details()