#!/usr/bin/python3


def print_list_integer(my_list=[]):
    a = len(my_list)
    if a == 0:
        print()
    else:
        for j in range(a):
            z = int(my_list[j])
            print("{:d}".format(z))
