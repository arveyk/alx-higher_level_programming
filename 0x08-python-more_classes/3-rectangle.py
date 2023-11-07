#!/usr/bin/python3
"""Class Rectangle that computes the area and perimeter of a tringle
    of given dimensions
"""


class Rectangle:
    """Rectangle class defines a rectangle of a certain height and width which
    are >= 0
    """
    def __init__(self, width=0, height=0):
        """Initialize every intatance object
            Args:
                width: the width of the rectagle
                height: the Height of the rectangle
            Returns: no return value
        """
#        if type(width) is int:
#            if width < 0:
#                raise ValueError('width must be >= 0')
        self.__width = width
#        else:
#            raise TypeError('width must be an integer')

#        if type(height) is int:
#            if height < 0:
#                raise ValueError('height must be >= 0')
        self.__height = height
#        else:
#            raise TypeError('height must be an integer')

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        wth = self.__width
        hgt = self.__height
        while (hgt > 0):
            p = 0
            for p in range(wth):
                print("#", end='')
            print()
            hgt -= 1
        return (f'{Rectangle.__name__}({self.__width}, {self.__height})')

    @property
    def width(self):
        """Getter: retrives the class attribute
            Returns: the width of the rectangle
            Setter: mutates the attributes
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter: gets the height attribute
            Returns: the height
            Setter: changes the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """calculates the area of a rectangle
            Args:
                None
            Returns: the area computed
            """
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of a rectangle
            Args:
                None
            Returns: the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height
