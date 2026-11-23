from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 1)

class Rectangle(Shape):

    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Dimensions must be positive")

        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Triangle(Shape):

    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Invalid triangle dimensions")

        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

def print_area(shape):
    print(f"{type(shape).__name__} Area: {shape.calculate_area()}")


circle = Circle(5)
rectangle = Rectangle(10, 5)
triangle = Triangle(10, 5)

print_area(circle)
print_area(rectangle)
print_area(triangle)
