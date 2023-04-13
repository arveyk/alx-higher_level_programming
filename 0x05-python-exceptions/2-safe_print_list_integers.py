#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    try:
        i = 1
        for i in range(x):
            c += 1
            print("{:d}".format(my_list[i]), end="")
        print()
        return (c)
    except TypeError:
        pass
    except ValueError:
        pass
