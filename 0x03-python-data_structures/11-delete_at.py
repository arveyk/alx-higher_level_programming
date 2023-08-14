#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    y = len(my_list) + 1
    x = 0
    for i in range(y):
        if x == idx:
            del(my_list[x])
        x += 1
    return my_list
