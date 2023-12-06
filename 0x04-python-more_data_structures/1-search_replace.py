#!/usr/bin/python3 
def search_replace(my_list, search, replace):
    def find(i):
        if i != search:
            return i
        else:
            return replace
    return (list(map(find, my_list)))

