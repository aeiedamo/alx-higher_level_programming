#!/usr/bin/python3
"""creating a Rectangle class"""


class Rectangle:
    """
    Not an empty one this time :)
    Args:
            width: width of Rectangle.
            height: height of Rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        super(Rectangle, self).__init__()
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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
            total += type(self).print_symbol * self.__width
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

    def __del__(self):
        """function for a class to delete its self"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect1, rect2):
        if not isinstance(rect1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect1.area() >= rect2.area():
            return rect1
        return rect2
