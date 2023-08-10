#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    y = len(argv) - 1
    if y == 1:
        print("{:d} argument:".format(y))
        print("{:d}: {:s}".format(y, argv[y]))
    elif y == 0:
        print("{:d} arguments.".format(y))
    else:
        print("{:d} argument:".format(y))
        for arg_s in range(1, y + 1):
            print("{:d}: {:s}".format(arg_s, argv[arg_s]))
