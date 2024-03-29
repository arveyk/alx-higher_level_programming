#!/usr/bin/python3
"""This Function prints the strings first_name and last_name
    It checks if the arguments passed are strings or not
"""


def say_my_name(first_name, last_name=""):
    """Prints name give to it
        Args:
            first_name: first string name
            last_name: second string name

        Returns:
            No return value
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    try:
        print("My name is {:s} {:s}".format(first_name, last_name))
    except Exception as e:
        print(e)
