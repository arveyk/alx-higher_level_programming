#!/usr/bin/python3
"""Class Rectagle defines a rectangle of a given height and given
    width
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
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """getter: retrives the class attribute
                Return: value of width
            setter: mutates the attributes
                Return: no value

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
