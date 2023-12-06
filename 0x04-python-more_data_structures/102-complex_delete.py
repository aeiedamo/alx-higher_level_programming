#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    todel = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            todel.append(key)
    for key in todel:
        del a_dictionary[key]
    return (a_dictionary)
