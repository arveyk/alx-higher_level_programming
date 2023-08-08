#!/usr/bin/python3
for char_t in range(122, 96, -1):
    if char_t % 2 != 0:
        char_t -= 32
    print("{:s}".format(chr(char_t)), end="")
