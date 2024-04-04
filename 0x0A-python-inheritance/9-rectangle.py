#!/usr/bin/python3
"""inintillizes the dimantions of figure whose area is to be computed
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class defining a rectangle
    """
    def __init__(self, width, height):
        """
        Args:
            width: how wide the rectangle is
            height: how long the rectangle is

        Returns: No return value
        """
        self.__width = width
        self.__height = height
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        # self.integer_validator('width', width)
        # self.integer_validator('height', height)

    def __str__(self):
        """ returns the string representation of rectangle class
            Args: none
            Return: informal string representation of class rectangle
        """
        return str(f'[Rectangle] {self.__width}/{self.__height}')

    def area(self):
        """ Calculates the area of a rectangle
            Args: No explicit return value
            Returns: the area
        """
        return self.__width * self.__height
