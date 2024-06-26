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
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the JSON  representation of list_dictionaries
            Args:
                list_dictionaries: list of dictionaries
            Returns: JSON repre of the list of dictionaries
        """
        if list_dictionaries is None:
            return []
        elif len(list_dictionaries) == 0:
            return []
        json_rep = json.JSONEncoder().encode(list_dictionaries)
        return json_rep
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON representation of list_objs
            Args:
                list_objs: list of instances that inherit from Base e.g.rect or
                sqr instances 
            Returns: No return value
        """
        if list_objs is None:
            list_objs = []
        else:
            to_json_string(list_objs)

    @staticmethod
    def from_json_string(json_string):
        """ Returns JSON string representation json_string
        """
        pass

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes set
        Args:
            cls:
            dictionary: key word args list of a dictionary
        """
        update(*arg, **kwargs)

    @classmethod
    def load_from_file(cls):
        """ Returns the list of instances
            Args:
                cls: current class using this method
            Returns: the list of instances, empty list if file does not exist
        """
        pass
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ For Serializing a file in CSC
        Args:
            cls:
            list_objs:
        Returns: serialised file
        """
        # format rect:  id, width, height, x, y
        #        sqr:   id, size, x, y
        pass

    @classmethod
    def load_from_file_csv(cls):
        """ For deserializing a CSV file
        Args:
            cls:
        Returns: No return value?
        """
        pass

    def draw(list_rectangles, list_squares):
        """ Opens a window and prints all the rectagles and squares
        Args:
            list_rectangles: list of rectangles to print
            list_squares: list of squares to print
        Returns: No return value
        """
        pass
