#!/usr/bin/python3
"""Class Square Package."""


class Square:
    """Class Square."""

    def __init__(self, size=0):
        """Square constructor."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
