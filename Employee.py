class Employee:

    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def display_id_card(self):
        print("Employee ID Card")
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Department:", self.department)


#input
name = input("Employee Name: ")
emp_id = input("Employee ID: ")
department = input("Department: ")

# Creating object
employee = Employee(name, emp_id, department)

# Displaying ID card
employee.display_id_card()