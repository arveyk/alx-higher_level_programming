#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        y = 0
        for i in range(x):
            y += 1
            print("{}".format(my_list[i]), end="")
        print()

    except IndexError:
        y -= 1
        print()

    return y

