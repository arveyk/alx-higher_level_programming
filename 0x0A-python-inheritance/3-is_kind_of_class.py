#!/usr/bin/python3
"""Function/Method to check if an object is an instance of a given object
"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class
        Args:
            obj: first class
            a_class: source/ root class
        Returns: True if it is
    """
    return isinstance(obj, a_class)
