#!/usr/bin/python3
"""
creating a square class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class,
    which inherits BaseGeometry"""

    def __init__(self, size):
        """Initializer method for square with size"""
        super().__init__(size, size)
        self.integer_validitor("size", size)
        self.__size = size

    def area(self):
        """method that returns area of a square"""
        return self.__size**2
