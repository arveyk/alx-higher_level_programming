#!/usr/bin/python3
"""Class square with the addition of an area public method"""


class Square:
    """Square class create a type that computes
    area of a square, when givena  size
    """
    def __init__(self, size=0):
        """
        Args:
            size: size of a square
        Return:
            No value
        """
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
