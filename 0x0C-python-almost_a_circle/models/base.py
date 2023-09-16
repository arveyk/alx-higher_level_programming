#!/usr/bin/python3
"""Module for defining a Base class
"""


class Base:
    """Class from which to inherit attributes
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """ class constructor
            Args:
                id: public instance attribute
            Returns: No return value
        """
        self.id = 0
        if id is not None:
            self.id = id
            self.__nb_objects = self.id
        else:
            Base.__nb_objects += 1
            id = self.__nb_objects
            self.id = self.__nb_objects
