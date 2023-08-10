#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum_of = 0
    y = len(argv)
    for num in range(1, y):
        sum_of += int(argv[num])
    print("{:d}".format(sum_of))
