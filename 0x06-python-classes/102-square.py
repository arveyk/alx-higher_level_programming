#!/usr/bin/python3
"""compare squares class"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """
        inintializes values for square
        Args:
            None
        Returns:
            no value
        """
        try:
            trial = size
            trial = trial + 2
            self.__size = size
        except TypeError:
            print('size must be a number')
        if size < 0:
            raise ValueError('size must be >= 0')
    
    def area(self):
        """computes area of square
            Args: 
                No parameter
            Return: 
                area of square
        """
        return self.__size ** 2
