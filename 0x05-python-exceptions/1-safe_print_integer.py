#!/usr/bin/python3


def safe_print_integer(value):
    try:
        if ord(value):
            print("{:d}".format(value))
            return True
    except:
        return False
