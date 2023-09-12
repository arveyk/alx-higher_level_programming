#!/usr/bin/python3
"""Module for appending content to a file
"""


def append_write(filename="", text=""):
    """function for appending to the text of a file
        Args:
            filename: name of file to append to
            text: content to append to file
        Returns: No return value
    """
    with open(filename, mode='a', encoding='utf-8') as app_f:
        count_chr = app_f.write(text)
        return count_chr
