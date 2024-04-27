#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return
    list_of_integers.sort(reverse=True)
    return list_of_integers[0]
