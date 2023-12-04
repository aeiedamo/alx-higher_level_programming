#!/usr/bin/python3
def multiple_returns(sentence):
    return_tuple = ()
    if sentence:
        return_tuple += (len(sentence), sentence[0])
    return (return_tuple)
