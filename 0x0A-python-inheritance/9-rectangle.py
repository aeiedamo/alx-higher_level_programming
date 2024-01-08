#!/usr/bin/python3
"""
creating a new Rectangle class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        calculate area of Rectangle
        """
        return self.__width * self.__height

    def __str__(self) -> str:
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
