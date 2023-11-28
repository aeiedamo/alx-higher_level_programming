#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        str = "{}{}".format(i, j)
        if i < j:
            print(str, end="")
            if str != "89":
                print(end=", ")
print()
