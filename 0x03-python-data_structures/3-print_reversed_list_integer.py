#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        print()
    else:
        my_list.reverse()
        for k in my_list:
            print("{:d}".format(k))
