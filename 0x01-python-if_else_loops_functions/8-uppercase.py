#!/usr/bin/python3


def uppercase(str):
    for y in str:
        if ord(y) >= 97 and ord(y) <= 122:
            p = ord(y) - 32
            y = chr(p)
        print("{}".format(y), end="")
    print()
