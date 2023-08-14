#!/usr/bin/python3


def no_c(my_string):
    new_str = ''
    for st in my_string:
        if st == 'C' or st == 'c':
            continue
        new_str += st
    return new_str
