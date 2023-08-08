#!/usr/bin/python3
def uppercase(str):
    conv = 32
    for uc in str:
        if ord(uc) >= 97 and ord(uc) <= 122:
            uc = chr(ord(uc) - conv)
        print("{:s}".format(uc), end="")
    print()
