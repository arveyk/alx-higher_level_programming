#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit


def main():
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif argv[2] == "-":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif argv[2] == "*":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif argv[2] == "/":
        print("{} + {} = {}".format(a, b, add(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main()
