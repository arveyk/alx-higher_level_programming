#!/usr/bin/python3
"""Function to add attribute"""


def add_attribute(obj, name, value):
    """ add_attribute adds an instance attribute if and only if it
    is possible
        Args:
            obj: the object to have an additional attribute
            name: name of the attribute
            value: the value of the attribute
        Return: No explicit return value
    """
    obj.name = value
    error = getattr(obj, name value)
    if (error == 'can\'t add new attribute'):
        raise TypeError('can\'t add new attribute')
