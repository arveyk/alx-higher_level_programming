#!/usr/bin/python3
"""Square module """


from models.rectangle import Rectangle

class Square(Rectangle):
    """ Defines a square, similar to a rectangle but 
        with width == height
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, width, height)
        self.width = width = size
        self.height = size
    def __str__(self):
        return f'[{Square}]'

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
