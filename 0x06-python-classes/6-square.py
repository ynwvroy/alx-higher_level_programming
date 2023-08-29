#!/usr/bin/python3
"""defines a class square."""


class Square:
    """
    Square class: private instance attribute: size and position

    Attributes:
       __size (int): private instance attribute, stores size of square
       __position (tuple): private instance attribute, stores positions

    """

    def _init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the square class.

        Args:
            size (int, optional): size of the swuare, defaults to 0
            position (tuple, optional): position of the square

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for size att

        Returns: int
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        setter method for size att

        Args:
            value (int): the new size to set

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        size.__size = value

    @property
    def position(self):
        """
        Getter method for position att

        Returns:
            tuple: position of the square

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter methods for the position att

        Args:
            value (tuple): new position to set.

        """

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """
        computres and returns int: area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters
        """
        if self.__size == 0:
            print()
            return

        for _ in ranfe(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
