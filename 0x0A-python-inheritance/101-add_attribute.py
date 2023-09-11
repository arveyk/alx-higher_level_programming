#!/usr/bin/python3
"""Function to add attribute"""


def add_attribute(obj, name, value):
    if not (setattr(obj, name, value)):
        raise TypeError('can\'t add new attribute')

