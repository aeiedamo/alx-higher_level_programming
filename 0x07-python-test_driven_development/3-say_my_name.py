#!/usr/bin/python3
"""
say_my_name: function to print first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name: function to print first_name and last_name
    Args:
        first_name: a string of a person's first name
        last_name: a string of a person's last name
    Returns:
        Nothing
    Raises:
        TypeError: exception with the message first_name must be a string or
         last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
