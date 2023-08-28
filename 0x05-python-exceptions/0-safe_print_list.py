#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            count += 1
            print("{}".format(my_list[i]), end="")
    except (IndexError):
        count -= 1
        pass
    print()
    return count