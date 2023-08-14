#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    list_b = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return list_b
    in_lst = 0
    for h in list_b:
        if in_lst == idx:
            list_b[idx] = element
        in_lst += 1
    return list_b
