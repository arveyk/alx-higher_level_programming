#!/usr/bin/python3
"""Module for writing an object to a text file
"""


def save_to_json_file(my_obj, filename):
    """function for writing a Object to text file using a JSON rep
    Args:
        my_obj: the object to be written to the file
        filename: the name of the file
    Returns: No value
    """
    import json
    with open(filename, mode='w', encoding='utf-8') as save_Json:
        json.dump(my_obj, save_Json)
