#!/usr/bin/python3
"""Checks if an object is inhrited
"""


def inherits_from(obj, a_class):
    """if obj is inherited from a_class it return True
        Args:
            obj: class to be evaluated
            a_class: (suspected to be)superclass
    """
    return issubclass(obj.__class__, a_class)
