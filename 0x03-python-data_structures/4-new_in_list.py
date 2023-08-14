#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    list_b = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return list_b
    for h in list_b:
        if h == idx:
            list_b[idx] = element
    return list_b
