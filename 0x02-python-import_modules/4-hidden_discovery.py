#!/usr/bin/python3
import hidden_4


def main():
    for st in dir(hidden_4):
        if ord(st[0]) == 95:
            continue
        print("{:s}".format(st))


if __name__ == "__main__":
    main()
