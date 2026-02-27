class SmartLight:
    def __init__(self, name):
        self.name = name
        self.status = "OFF"

    def set_status(self, action):
        self.status = action

    def display(self):
        print(f"{self.name} is {self.status}")

name = input("Light Name: ")
action = input("Action: ").upper()

light = SmartLight(name)
light.set_status(action)
light.display()