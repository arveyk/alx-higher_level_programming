#!/usr/bin/python3
""" Square Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square definition"""
    def __init__(self, size):
        """ initialization for every square object
            Args:
                size: dimentions of the square
            Returns: no explicit return value
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
        self.area()
