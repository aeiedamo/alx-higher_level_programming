#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    mod = number % 10
else:
    mod = (-1 * number) % 10
print("Last digit of", number, "is", mod, end=" ")
if mod > 5:
    print("and is greater than 5")
elif mod == 0:
    print("and is 0")
elif mod < 6 and mod != 0:
    print("and is less than 6 and not 0")
