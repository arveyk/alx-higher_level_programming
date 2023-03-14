#!/usr/bin/python3
import sys

def main():
    n = len(sys.argv)
    summ = 0
    if n == 1:
        print("{:d}".format(summ))
    else:
        for i in range(1, n):
            summ += int(sys.argv[i])
        print("{:d}".format(summ))


if __name__ == "__main__":
    main()
