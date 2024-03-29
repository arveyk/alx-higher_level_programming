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
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        '''return str('Rectangle({self.__width}, {self.__height})')'''
