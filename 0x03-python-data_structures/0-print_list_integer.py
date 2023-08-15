#!/usr/bin/python3


def print_list_integer(my_list=[]):
    if my_list is None:
        pass
    else:
        a = len(my_list)
        for j in range(a):
            print("{:d}".format(my_list[j]))
