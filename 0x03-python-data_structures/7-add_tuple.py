#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    len_1 = len(tuple_a)
    len_2 = len(tuple_b)
    a, b, f, g = 0, 0, 0, 0
    if len_1 == 1 and len_2 >= 2:
        a = tuple_a[0]
    elif len_1 >= 2:
        a, b = tuple_a[0], tuple_a[1]
    if len_2 == 1:
        f = tuple_b[0]
    elif len_2 >= 2:
        f, g = tuple_b[0], tuple_b[1]
    m, n = (a + f), (b + g)
    tuple_z = m, n
    return tuple_z
