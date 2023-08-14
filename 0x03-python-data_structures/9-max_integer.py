#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    q = 0
    for gr in my_list:
        if gr > q:
            q = gr
    return q
