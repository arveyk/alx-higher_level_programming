#!/usr/bin/python3


class MagicClass:
    import math
    def __init__(self, radius):
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
    def area(self):
        return 2 ** self.__radius * math.pi
    def circumference(self):
        return 2 * self.__radius * math.pi
