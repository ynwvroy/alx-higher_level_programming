#!/usr/bin/python3
"""method Rectangle(Base Geometry)"""


class Rectangle(BaseGeometry):
    """Class of a Rectangle"""

    def __init__(self, width, height):
        """
        Initialize a rectangle Instance

        Args:
            width (int): the width of a rectangle
            height (int): the height of a rectangle

        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
