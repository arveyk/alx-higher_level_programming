#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        v = int(a)
    except Exception as d:
        d = "a must be an integer"
        return d
    try:
        q = int(b)
    except Exception as d:
        d = "b must be an integer"
        return d
    return v + q
