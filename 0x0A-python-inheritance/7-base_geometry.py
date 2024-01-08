#!/usr/bin/python3
"""
an empty class BaseGeometry.
"""


class BaseGeometry:
    """
    an empty class BaseGeometry.
    """

    @classmethod
    def area(self):
        """
        class method to calculate area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method to validate if number is an integer
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
