#!/usr/bin/python3
"""
a function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    method to check if an object is an instance of a class that it
    inherited from
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
