#!/usr/bin/python3
"""Class with private instance attribute"""


class Square:
    """Class Square demonstrate a private instance attribute
    """
    def __init__(self, size):
        """__init__ initializes the private instance attribute

        Args:
            size: size of a square, an integer
        """
        self.__size = size
