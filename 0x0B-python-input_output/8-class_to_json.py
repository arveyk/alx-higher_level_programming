#!/usr/bin/python3
"""Module for converts an Object tot dictionary
"""


def class_to_json(obj):
    """return dictionary for JSON serialization of an object
        Args:
            obj: the class object
        Returns: the dictionary description
    """
    return dict(obj.__dict__)
