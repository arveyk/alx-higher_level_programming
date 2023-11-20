#!/usr/bin/python3
''' Class square definition '''
Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    ''' Square, special kind of rectangle
    '''
    def __init__(self, size):
        super().__init__(size, size)
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        return super().area()

    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'
