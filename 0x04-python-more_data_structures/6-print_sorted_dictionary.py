#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        pass
    else:
        sort_of = sorted(a_dictionary)
        for m in sort_of:
            print("{:s}: {}".format(m, a_dictionary[m]))
