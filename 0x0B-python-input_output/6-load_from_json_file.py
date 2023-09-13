#!/usr/bin/python3
"""Module for decoding JSON str from a file
"""


def load_from_json_file(filename):
    """reads from JSON file and converts to a Object
    Args:
        filename: name of the file to be read from
    Returns: Object, the decoded JSON string
    """
    import json
    with open(filename, mode="r", encoding='utf-8') as from_json:
        obj = json.load(from_json)
        return obj
