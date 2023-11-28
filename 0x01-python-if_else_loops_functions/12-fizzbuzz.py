#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            if i % 3 == 0:
                print("Fizz", end="")
            else:
                print("Buzz", end="")
        else:
            print(i)
        print(end=" ")
    print()
