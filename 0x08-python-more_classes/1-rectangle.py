#!/usr/bin/python3
"""creating a Rectangle class"""


class Rectangle:
    """
    Not an empty one this time :)
    Args:
            width: width of Rectangle.
            height: height of Rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialize data components"""
        super(Rectangle, self).__init__()
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter function for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter function for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter function for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
