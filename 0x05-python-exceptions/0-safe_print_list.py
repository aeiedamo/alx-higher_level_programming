#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    for count in my_list:
        try:
            if (printed >= x):
                break
            print("{:d}".format(count), end="")
            printed += 1
        except Exception:
            continue
    print()
    return (printed)
