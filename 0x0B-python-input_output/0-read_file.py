#!/usr/bin/python3
"""
a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Print content of a file with utf-8 encoding"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
