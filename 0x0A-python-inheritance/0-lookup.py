#!/usr/bin/python3
"""
a function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """
    lookup(obj): a function that returns the list of available
    attributes and methods of an object.

    Args: obj
    Returns: list object
    """
    return dir(obj)
