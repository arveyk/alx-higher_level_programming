#!/usr/bin/python3

import add_0

a = 1
b = 2

def addi(a, b):
    plus = add_0.add(a, b)
    print("{}".format(plus))

def main():
    addi(a, b)

if __name__ == "__main__":
    main()

