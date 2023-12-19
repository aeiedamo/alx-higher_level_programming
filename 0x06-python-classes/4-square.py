#!/usr/bin/python3
"""
Defining a Square class
"""


class Square:
    """
    Defining a self call
    Args:
        size: length of square
    """
    def __init__(self, size=0):
        """
        initailizing for square
        Args:
            size: length of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        A function to find area of Square
        Return: the size squared
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        a function to return square size
        Return: size of square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        a function to set property of Square
        Args: size => length of square
        Raise:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
