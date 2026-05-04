#Day 29 - Inheritance Helper
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand} started"

class Car(Vehicle):
    def drive(self):
        return "Driving car!"

my_car = Car("Toyota")
print(my_car.start())
print(my_car.drive())