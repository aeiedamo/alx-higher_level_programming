#!/usr/bin/python3
"""
print_square: to print a square
"""


def print_square(size):
    """
    print_square: to print a square with the character '#'
    Args:
        size: size of square
    Returns:
        Nothing
    Raises:
        TypeError: exception with the message size must be an integer
        ValueError: exception with the message size must be >= 0
        TypeError: exception with the message size must be an integer
         if size is float
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print((("#" * size) + "\n") * size, end="")
