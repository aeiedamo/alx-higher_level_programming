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
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter function for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __repr__(self) -> str:
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __str__(self) -> str:
        """Returns a representation for a Rectangle in text"""
        total = ""
        if self.__width == 0 or self.__height == 0:
            return total
        for i in range(self.__height):
            total += "#" * self.__width
            if i != self.__height - 1:
                total += "\n"
        return total

    def area(self):
        """Getter for area value"""
        return self.__width * self.__height

    def perimeter(self):
        """Getter for perimeter value"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
