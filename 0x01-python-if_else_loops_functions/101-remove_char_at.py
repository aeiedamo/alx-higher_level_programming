#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for i in str:
        if n <= len(str) && n >= 0:
            if i != str[n]:
                new += i
        else:
            new += i
    return (new)
