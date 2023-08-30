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
        if size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        """Value getter and setter
        getter: retrieves the value of size
        setter: changes the dimensions of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        self.__size = value
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """area method computes the area of a square

        Args:
            None
        Returns:
            Area of a square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints square pattern
        Args:
            None
        Returns:
            no Value
        """
        val = self.__size
        if val == 0:
            print()
        else:
            for i in range(val):
                print()
                for u in range(val):
                    print("#", end="")
            print()
