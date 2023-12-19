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
    def __init__(self, size=0, position=(0, 0)):
        """
        initailizing for square
        Args:
            size: length of square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        a function to retreive position
        Return: position of square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        function to set value for position
        Args: value => position for square
        Raise: TypeError("position must be a tuple of 2 positive integers")
        """
        if (type(value) != tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) and type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] and value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        function that prints in stdout the square with the character #
        """
        if (self.__size == 0):
            print()
        else:
            for i in range(self.position):
                print()
            for i in range(self.size):
                print(" " * self.position, end="")
                print("#" * self.size)
