#!/usr/bin/python3
"""creating a Rectangle class"""


class Rectangle:
    """
    Not an empty one this time :)
    attributes: width, height.
    """

    def __init__(self, width=0, height=0):
        super(Rectangle, self).__init__()
        self.__width = width
        self.__height = height

    """getter function for width"""

    @property
    def width(self):
        return self.__width

    """setter function for width"""

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """getter function for height"""

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
