#!/usr/bin/python3
"""Class Square Package."""
class Square:
    """Class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Square Constructor."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Position - getter."""
        return self.__position

    @position.setter
    def position(self, value):
        """Position - setter."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """My_print - function that render the area of the square using # character."""
        if self.__size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for _ in range(self.__size):
            print('{}'.format(' ' * self.position[0] + '#' * self.__size))
