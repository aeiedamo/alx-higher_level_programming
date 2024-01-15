#!/usr/bin/python3
"""creating a Rectangle class"""
from models.base import Base
import unittest


class Rectangle(Base):
    """a Rectangle Class that inherts from Base"""

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        """Initializer for Rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x"""
        self.validator("x", value, True)
        self.x = value

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """, valueSetter method for y"""
        self.validator("y", value, True)
        self.y = value

    def validator(self, name, value, x_y=False):
        """validator for setter methods"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and not x_y:
            raise ValueError("{} must be > 0".format(name))
        elif value < 0 and x_y:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """method to return area of Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Method to print to stdout Rectangle with #"""
        print("\n" * self.__y, end="")
        print("\n".join([" " * self.__x + "#" * self.__width] * self.__height))

    def __str__(self) -> str:
        """Method to return [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__,
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height,
        )

    def __update__(self, id=None, width=None, height=None, x=None, y=None):
        """Method to update all atributes"""
        if id is not None:
            self.id = id
        if width is not None:
            self.__width = width
        if height is not None:
            self.__height = height
        if x is not None:
            self.__x = x
        if y is not None:
            self.__y = y

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes"""
        if args:
            self.__update__(*args)
        elif kwargs:
            self.__update__(**kwargs)

    def to_dictionary(self):
        """to convert a Rectangle to dictionary"""
        return {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width,
        }
