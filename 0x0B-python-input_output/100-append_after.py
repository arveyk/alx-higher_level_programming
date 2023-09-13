#!/usr/bin/python3
"""Module of func that appends after  a specific string
"""


def append_after(file_name="", search_string="", new_string=""):
    """appends new_string to a file after encounterting a specific string
    Args:
        file_name: name of the file to append
        search_string: the file to append
        new_string: the string to write to a file

    Return: No ret value
    """
    append_num = 0
    c_read = len(search_string)
    import json
    with open(file_name, mode="a+") as ap_nd:
        comp_r = ap_nd.read(c_read)
        while len(comp_r) > 0:
            if comp_r == search_string:
                ap_nd.write(new_string)
            comp_r = ap_nd.read(c_read)

