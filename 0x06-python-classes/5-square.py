#!/usr/bin/python3
"""Class Square Package."""


class Square:
    """Class Square."""

    def __init__(self, size=0):
        """Square Constructor."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area - method that calculates area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Size - getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Size - setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """My_print - function that render the area of the square."""
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            print('{}'.format('#' * self.__size))
