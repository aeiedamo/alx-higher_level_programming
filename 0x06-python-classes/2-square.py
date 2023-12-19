#!/usr/bin/python3
""" Define a square class """


class Square:
    """
    Class to define what a square is
    Args:
        size: length of square
    """

    def __init__(self, size):
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
