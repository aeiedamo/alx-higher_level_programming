#!/usr/bin/python3
from sys import *


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=stderr)
        return (None)
    return (result)
