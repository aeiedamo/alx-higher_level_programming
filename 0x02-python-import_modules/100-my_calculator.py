#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = len(sys.argv) - 1
    if i != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operation = sys.argv[2]
    if operation not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if operation == '+':
        print("{} {} {} = {}". format(a, operation, b, add(a, b)))
    elif operation == '-':
        print("{} {} {} = {}". format(a, operation, b, sub(a, b)))
    elif operation == '*':
        print("{} {} {} = {}". format(a, operation, b, mul(a, b)))
    elif operation == '/':
        print("{} {} {} = {}". format(a, operation, b, div(a, b)))
