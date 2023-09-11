#!/usr/bin/python3
"""inintillizes the dimantions of figure whose area is to be computed
"""

class Rectangle(BaseGeometry):
    """class defining a rectangle
    """
    def __init__(self, width, height):
        super().__init__()

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

        return str('Rectangle({self.__width}, {self.__height})')
