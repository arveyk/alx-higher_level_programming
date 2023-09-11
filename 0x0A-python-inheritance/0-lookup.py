#!/usr/bin/python3
"""Function to return the attribute and methods of an object
"""


def lookup(obj):
    """Returns the attributes and methods of an object
        Args:
            obj: the object to be evaluated
        Return: list of attributes an objects
    """
    return list(dir(obj))
