#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_string = my_string.replace("C", "")
        new_string = my_string.replace("c", "")
        return (new_string)
    return (my_string)
