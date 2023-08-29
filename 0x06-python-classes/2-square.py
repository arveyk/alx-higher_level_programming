#!/usr/bin/python3
"""Class with private instance attribute
There is an additional optional size: def __init__(self, size=0):
"""


class Square:
    """Class Square demonstrate a private instance attribute

    """
    def __init__(self, size=0):
        """__init__ initializes the private instance attribute

        Args:
            size: size of a square, an integer
        Return:
            No value
        """
        self.__size = (size)
        if type(size) is not int:
            raise TypeError('size must be an integer:')
        if size < 0:
            raise ValueError("size must be >= 0")
