#!/usr/bin/python3
"""Square module """


from models.rectangle import Rectangle
from models.base import Base

class Square(Rectangle, Base):
    """ Defines a square, similar to a rectangle but 
        with width == height
    """
    def __init__(self, size, x=0, y=0, id=None):
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y
        Rectangle().__init__(id, width, height, x=0, y=0)
        Base().__init__(id, width, height, x=0, y=0)

    def __str__(self):
        return f'[{Square}]'

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
