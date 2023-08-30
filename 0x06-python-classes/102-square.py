#!/usr/bin/python3
"""properties getters and setters demo"""


class Square():
    """computes area of a square"""
    def __init__(self, size=0):
        """
        Args:
            size: size of a square
        Return:
            No value
        """
        try:
            size / 2
            self.__size = size
        except Exception as e:
            print("size must be a number", e)
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

    def __lt__(self, compareWith):
        """ compares if square a is less than square b"""
        return self.__size ** 2 < compareWith.__size ** 2

    def __le_(self, compareWith):
        """ compares if square a is less than square b"""
        return self.__size ** 2 <= compareWith.__size ** 2

    def __eq__(self, compareWith):
        """ compares if square a is less than square b"""
        return self.__size ** 2 == compareWith.__size ** 2

    def __ne__(self, compareWith):
        """ compares if square a is less than square b"""
        return self.__size ** 2 != compareWith.__size ** 2

    def __gt__(self, compareWith):
        """ compares if square a is less than square b"""
        return (self.size ** 2) > (compareWith.size ** 2)

    def __ge__(self, compareWith):
        """ compares if square a is less than square b"""
        return self.__size >= compareWith.__size

    def area(self):
        """area method computes the area of a square

        Args:
            None
        Returns:
            Area of a square
        """
        return self.__size ** 2
