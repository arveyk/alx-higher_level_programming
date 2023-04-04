#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        c = 0
        for i in range(x):
            if ((ord(i) >= 65 and ord(i) <= 90) or \
                    (ord(i) >= 97 and ord(i) <= 122)):
                continue
            c += 1
            print("{:d}".format(my_list[i]), end="")
        print()
        return c
    except IndexError:
        print()
    except TypeError:
        print()
