#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """
    Square class: private instance attribute: size.

    Attributes:
       __size (int): the private instance attribute
    """

    def __init__(self, size=0):
        """
        Initialize a new instance of Square class.

        Args:
            size (int, optional): the size of the square
        """
        self.__size = size
    @property
    def size(self):
        """Getter method for the size attribute.


        Returns:
            int: the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter method for the size attribute.

        Args:
            value (int): the new size to set.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        computes and returns the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints the square using '#' characters
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
