#!/usr/bin/python3
"""
Square class defining a square type that computes area of a sqr
it checks for valid dimentions

"""


class Square:
    """
    computes area of a square
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

    @property
    def size(self):
        """Value getter and setter
        getter: retrieves the value of size
        setter: changes the dimensions of square
        Type: int
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        self.__size = value
        if value < 0:
            raise ValueError('size must be >= 0')

        if len(self.__position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        
    def area(self):
        """area method computes the area of a square

        Args:
            None
        Returns:
            Area of a square
        """
        return self.__size ** 2
