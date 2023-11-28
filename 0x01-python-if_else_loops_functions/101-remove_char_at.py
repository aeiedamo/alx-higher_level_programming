#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for i in str:
        if i != str[n]:
            new += i
    return (new)
