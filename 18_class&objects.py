class Car:
    # Constructor: runs when you create a new object
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # Method: an action the object can do
    def drive(self):
        print(f"The {self.color} {self.brand} is driving!")

# Create objects
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

# Access attributes
print(car1.brand)   # Output: Toyota
print(car2.color)   # Output: Blue

# Call methods
car1.drive()  # Output: The Red Toyota is driving!
car2.drive()  # Output: The Blue Honda is driving!
