#!/usr/bin/python3
"""Magic class for disassembyl"""


class MagicClass:
    """Magic class calculates the area and peremeter of a circle
    Checks if radius given is a number and if it is positive
    """
    import math

    def __init__(self, radius=0):
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """Computes the area of a circle
            Args: No arguments here
            Return: The area computed
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Computes the peremeter of a circle of given size
            Args: No other argument
            Return: The peremeter of a circle of given size
        """
        return 2 * self.__radius * math.pi
