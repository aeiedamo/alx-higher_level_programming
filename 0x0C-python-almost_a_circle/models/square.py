#!/usr/bin/python3
"""Creating a Square Class"""
from models.rectangle import Rectangle
import unittest


class Square(Rectangle):
    """A class to create a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """An initializer for Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size"""
        self.width = value
        self.height = value

    def __str__(self) -> str:
        """returns a string representation of Square"""
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x, self.y, self.size
        )

    def to_dictionary(self):
        """returns a dictionary of Square"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}

    def __update__(self, id=None, size=None, x=None, y=None):
        """to update values of Square"""
        return super().__update__(id, size, size, x, y)

    def update(self, *args, **kwargs):
        """to updaye values of Square with key/value pairings"""
        if args:
            return self.__update__(*args)
        elif kwargs:
            return self.__update__(**kwargs)
