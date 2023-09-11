#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
is inherits_from(a, int):
    print("{} inherits from class {}".format(a, int.__name__))
is inherits_from(a, bool):
    print("{} inherits from class {}".format(a, bool.__name__))
is inherits_from(a, object):
    print("{} inherits from class {}".format(a, object.__name__))
