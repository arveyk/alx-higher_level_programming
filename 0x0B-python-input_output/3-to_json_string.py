#!/usr/bin/python3
"""conversion to json, Module
"""


def to_json_string(my_obj):
    """returns json representation of an object(string)
        Args:
            my_obj: the object to be converted
        Returns: the JSON rep of the object
    """
    import json
    return json.dumps(my_obj)
