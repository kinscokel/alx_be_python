# polymorphism_demo.py

import math

# Base Class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area() method.")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Example usage (optional demonstration)
if __name__ == "__main__":
    shapes = [
        Rectangle(4, 5),
        Circle(3)
    ]

    for shape in shapes:
        print(f"The area is: {shape.area():.2f}")