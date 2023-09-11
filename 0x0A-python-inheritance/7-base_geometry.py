#!/usr/bin/python3
"""In this BaseGeometry, the area method is implemented

"""


class BaseGeometry():
    """Computes area based on mesurement given
    """

    def area(self):
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(' name must be an integer')
        if value <= 0:
            raise ValueError('name must be greater than 0')
