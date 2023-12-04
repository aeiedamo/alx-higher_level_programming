#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list and idx in range(len(my_list)):
        my_list.remove(my_list[idx])
    return (my_list)
