#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 0:
        return tuple_a
    if len(tuple_b) == 0:
        a = tuple_a[0] + 0
    a = tuple_a[0] + tuple_b[0]
    if len(tuple_b) <= 1:
        b = tuple_a[1] + 0
    else:
        b = tuple_a[1] + tuple_b[1]
    t = (a, b)
    return t
