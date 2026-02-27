class Contact:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display_contact(self):
        print("Contact Saved")
        print("Name:", self.name)
        print("Phone:", self.phone)


# Taking input
name = input("Contact Name: ")
phone = input("Phone Number: ")

# Creating object
contact = Contact(name, phone)

# Displaying contact information
contact.display_contact()