#!/usr/bin/python3
"""a function that adds a new attribute to an object if it’s possible:"""


def add_attribute(object, name, value):
    """a function to set object's attribute named name to value"""
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, name, value)
