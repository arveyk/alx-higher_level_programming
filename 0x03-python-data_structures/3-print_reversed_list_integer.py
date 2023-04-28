#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    i = len(my_list) + 1
    j = -1
    while abs(j) < i:
        print("{:d}".format(my_list[j]))
        j -= 1
