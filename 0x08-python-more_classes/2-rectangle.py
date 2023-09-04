#!/usr/bin/python3
"""Defines the class Rectangle."""


class Rectangle:
    """
    class represents a rectangle

    Att:
       width (int)
       height (int)
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle instance

        Args:
            width(int)
            height(int)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Int: the width of the rectangle.
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
        int: height of the rectangle
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

    def area(self):
        """
        calculate and return the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculate and returnn the perimeter of the rectangle
        """
        return 2 * (self.__width + self.__height)
