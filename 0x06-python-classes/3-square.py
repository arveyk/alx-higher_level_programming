#!/usr/bin/python3
"""Class square with the addition of an area public method"""


class Square:
    def __init__(self, size=0):
        '''
        Args:
            size: size of a square
        '''
        try:
            self.__size = size
        except Exception as e:
            print("size must be an integer", e)
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """area method computes the area of a square

        Args:
            None
        Returns:
            No value
        """
        return self.__size ** 2
