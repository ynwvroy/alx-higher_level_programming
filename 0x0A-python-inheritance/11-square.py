#!/usr/bin/python3
"""
This module defines geometric classes for calculating areas.
"""


class GeometryError(Exception):
    """Custom exception for geometry errors"""
    pass


class BaseGeometry:
    """Base class for geometry"""
    def area(self):
        """Calculate the area of a geometric shape."""
        raise GeometryError("Area calculation is not implemented.")

    def validate_integer(self, name, value):
        """Validate that a value is a positive integer."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer.")


class Rectangle(BaseGeometry):
    """Class representing a rectangle."""
    def __init__(self, width, height):
        self.validate_integer("width", width)
        self.validate_integer("height", height)
        self._width = width
        self._height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self._width * self._height

    def __str__(self):
        return f"[Rectangle] {self._width}/{self._height}"


class Square(Rectangle):
    """Class representing a square (a special rectangle)."""
    def __init__(self, size):
        super().__init__(size, size)
        self._size= size

    def __str__(self):
        return f"[Square] {self._size}/{self._size}"


    if __name__ == "__main__":
        r = Rectangle(3, 5)
        print(r)
        print(f"Area: {r.area()}")

        s = Square(4)
        print(s)
        print(f"Area: {s.area()}")
