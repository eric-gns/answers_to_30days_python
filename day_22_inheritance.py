# ==========================================
# DAY 22: INHERITANCE AND POLYMORPHISM
# ==========================================

# Base Parent Class
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"{self.year}, {self.brand}"


# Child Class (Inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def info(self):
        return f"{super().info()} with {self.doors} doors"


# Multi-level Child Class (Inherits from Car)
class ElectricCar(Car):
    def __init__(self, brand, year, doors, battery_capacity):
        super().__init__(brand, year, doors)
        self.battery_capacity = battery_capacity

    def info(self):
        return f"{super().info()} (Battery: {self.battery_capacity})"


# Polymorphic execution across mixed object types
vehicles = [
    Vehicle("Generic Brand", 2018),
    Car("Toyota", 2022, 4),
    ElectricCar("Tesla", 2024, 4, "75kWh")
]

for v in vehicles:
    print(v.info())