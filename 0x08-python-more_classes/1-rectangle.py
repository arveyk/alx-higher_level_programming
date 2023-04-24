#!/usr/bin/python3
""" Retangle function that does no action"""


class Rectangle:
    """Rectangle class with private attribute"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Property to return width"""
        return self.__width

    @width.setter
    def width(self, value):
        try:
            self.__width = value
            if value < 0:
                raise ValueError('width must be >= 0')
        except TypeError:
            print("must be an integer")

    @property
    def height(self):
        """Height of the rectangle returned"""
        return self.__height

    @height.setter
    def height(self, value):
        try:
            self.__height = value
            if value < 0:
                raise ValueError('height must be >= 0')
        except TypeError:
            print("must be an integer")
