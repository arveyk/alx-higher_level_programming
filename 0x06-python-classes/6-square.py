#!/usr/bin/python3
"""
Square class defining a square type that computes area of a sqr
it checks for valid dimentions

"""


class Square:
    """
    computes area of a square
    """
    def __init__(self, size=0, position=(0, 0)):
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
        if type(position) is tuple:
            if len(position) == 2:
                if type(position[0]) is int and type(position[1]) is int:
                    self.__position = position
        else:
            raise TypeError("must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """
        getter: retrieves value named position
        setter: mutates position attribute
        Type: tuple
        """
        return self.__position

    @position.setter
    def position(self, value):
        """if type(value) is tuple:
            if len(value) == 2:
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')
        """
        try:
            self.__position = value
        except Exception as e:
            print("position must be a tuple")

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
        """ alias value for __size"""
        val2 = self.__position[0]
        """ alias value for 1st argument int tuple"""
        val3 = self.__position[1]
        """ alias value for 2nd argument int tuple"""
        try:
            type(val2 + val3) is int
        except Exception as e:
                print('position must be a tuple of 2 positive integers', e)
        if val == 0:
            print()
        else:
            if val3 is not None:
                b = 0
                while b < val3:
                    print()
                    b += 1
            for i in range(val):
                print(" " * val2, end="")
                for u in range(val):
                    print("#", end="")
                if i < val - 1:
                    print()
            print()
