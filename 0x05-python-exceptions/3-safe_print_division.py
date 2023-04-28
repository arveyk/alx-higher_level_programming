#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = 0
        res = a / b
        return res

    except ZeroDivisionError:
        pass

    finally:
        if b == 0:
            print("Inside result: None")
        else:
            print("Inside result: {:.1f}".format(res))
