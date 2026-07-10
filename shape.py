
import math

class Shape:
    """A class representing a geometric shape."""

    def __init__(self, color: str, name: str):
        self.color = color
        self.name = name

    def say_name(self):
        return f"My name is {self.name}."


class Rectangle(Shape):
    """A class representing a rectangle, inheriting from Shape."""

    def __init__(self, color: str, name: str, width: float, height: float):
        super().__init__(color, name)
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def say_name(self):
        return f"My name is {self.name} and I am a rectangle."


class Circle(Shape):
    """A class representing a circle, inheriting from Shape."""

    def __init__(self, color: str, name: str, radius: float):
        super().__init__(color, name)
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return 3.14 * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * 3.14 * self.radius

    def say_name(self):
        return f"My name is {self.name} and I am a circle."
