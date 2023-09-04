#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """
    This class rep a rectangle.

    Att:
       width (int): width of rectangle
       height (int): height of a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle instance.

        Args:
            width
            height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Int: width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
