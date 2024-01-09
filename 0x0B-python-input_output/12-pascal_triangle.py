#!/usr/bin/python3
"""pascal_numbers returns a list of lists of integers
representing the Pascal’s triangle of n"""


def _factorial_(n):
    """finds factorial of n"""
    if n <= 1:
        return 1
    return _factorial_(n - 1) * n


def comb(i, j):
    """finds an element for a row in pascal numbers triangle"""
    return int(_factorial_(i) / (_factorial_(j) * _factorial_(i - j)))


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    pascal_numbers = []
    if n <= 0:
        return pascal_numbers
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(comb(i, j))
        pascal_numbers.append(row)
    return pascal_numbers
