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
        
        try:
            self.__position = position
        except Exception as e:
            print("position must be a tuple of 2 positive integers", e)

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
    
    @property
    def position(self):
        """Value getter and setter
        getter: retrieves the value of position
        setter: changes the value of position
        Type: int
        """
        return self.__size

    @position.setter
    def size(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integer")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")

        
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
            for psn in range(self.__position[1]):
                print(" ")
            for i in range(val):
                print(" " * self.__position[0], end="")
                for u in range(val):
                    print("#", end="")
                if i < val - 1:
                    print()

    def __repr__(self):
        return f'{Square.my_print(self)}'
