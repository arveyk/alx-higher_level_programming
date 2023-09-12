#!/usr/bin/python3
"""Module for wrinting to a file
"""


def write_file(filename="", text=""):
    """This function opens a file and writes a text to it
        Args:
            filename: name of the file to be written to
            text: the text to write to the file
        Returns: No return value
    """
    with open(filename, mode='w', encoding='utf-8') as w_f:
        w_count = w_f.write(text)
        return w_count
