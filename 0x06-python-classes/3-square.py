#!/usr/bin/python3
"""Square class that defines a private instance attribute size"""


class Square:
    """size: size of a square"""
    def __init__(self, size=0):
        try:
            self.__size = size
            if size < 0:
                raise ValueError('size must be >= 0')
        except TypeError:
            print("size must be an integer")

    def area(self):
        """Calculates the area of a square give the dimension, size"""
        return self.__size * self.__size
