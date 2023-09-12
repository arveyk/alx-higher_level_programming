#!/usr/bin/python3
"""Modele for returning an object represented by JSON string
"""


def from_json_string(my_str):
    """Converts JSON string to python object
        Args:
            my_str: the string to convert
        Return: object rep of the string

    """
    import json
    return json.loads(my_str)
