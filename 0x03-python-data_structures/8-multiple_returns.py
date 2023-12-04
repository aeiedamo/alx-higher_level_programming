#!/usr/bin/python3
def multiple_returns(sentence):
    return_tuple = ()
    if sentence:
        return_tuple += (len(sentence), sentence[0])
    else:
        return_tuple += (0, None)
    return (return_tuple)
