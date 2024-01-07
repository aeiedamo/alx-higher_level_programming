#!/usr/bin/python3
"""
add_integer(a, b=98):
function to add 2 numbers (integers or floats)
returns the sum of the 2 numbers
"""


def add_integer(a, b=98):
    """
    a function to add 2 integers and return result
    Args:
        a: an integer or a float
        b: an integer or a float
    Returns:
        the sum of a and b
    Raises:
        a TypeError exception with the message a must be
        an integer or b must be an integer
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
