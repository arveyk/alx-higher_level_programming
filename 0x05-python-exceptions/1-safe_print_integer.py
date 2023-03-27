#!/usr/bin/python3


def safe_print_integer(value):
    try:
        if ord(value):
            return True
    except TypeError:
        return False
