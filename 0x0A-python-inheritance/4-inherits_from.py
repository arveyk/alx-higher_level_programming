#!/usr/bin/python3
"""Checks if an object is inhrited
"""


def inherits_from(obj, a_class):
    """if obj is inherited from a_class it return True
        Args:
            obj: class to be evaluated
            a_class: (suspected to be)superclass
    """
    if issubclass(obj.__class__, a_class):
        if issubclass(a_class, obj.__class__) is not True:
            return True
    return False
