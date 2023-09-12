#!/usr/bin/python3
""" File reading module
"""


def read_file(filename=""):
    """this function opens and reads a file within a with construct
        Args:
            filename: name of the file
        Returns: No return value
    """
    with open(filename, encoding='utf-8') as file_name:
        chars = file_name.read()
        print('{}'.format(chars), end="")
