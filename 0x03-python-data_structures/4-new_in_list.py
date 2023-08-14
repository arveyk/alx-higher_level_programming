#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    list_b = my_list[:]
    for h in list_b:
        if h == idx:
            list_b[idx] = element
    return list_b
