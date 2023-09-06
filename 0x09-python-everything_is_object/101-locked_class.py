#!/usr/bin/python3
"""Creating a Locked class
    __slots__ is used to avoid dynamically created attributes
"""


class LockedClass(object):
    """Creation of a Locked class, new instance attributes have to be
        called first_name
    """

    __slots__ = ['first_name']

    def __init__(self, first=None):
        """Initializes the instance attributes,
        Args:
            first: name of the varible locked to first_name
        Return: No value
        """
        self.first_name = first
