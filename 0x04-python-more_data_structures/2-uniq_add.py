#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq = set(my_list)
    add_un = 0
    for h in uniq:
        add_un += h
    return add_un
