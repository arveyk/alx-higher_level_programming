#!/usr/bin/python3
"""Module for defining a Base class
"""
import csv
import json
import os
import turtle


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
            return "[]"
        elif len(list_dictionaries) == 0:
            return "[]"
        json_rep = json.JSONEncoder().encode(list_dictionaries)
        return json_rep

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON representation of list_objs
            Args:
                list_objs: list of instances that inherit from Base e.g.rect or
                sqr instances
            Returns: No return value
        """
        strData = []
        if list_objs is None:
            strData = '[]'
        else:
            objData = []
            for ob in list_objs:
                objData.append(ob.to_dictionary())
            strData = cls.to_json_string(objData)

        fileName = cls.__name__ + ".json"
        with open(fileName, mode="wt") as f:
            f.write((strData))

    @staticmethod
    def from_json_string(json_string):
        """ Returns list of JSON string representation json_string
        """
        if json_string is None:
            return []
        if len(json_string) == 0:
            return []
        return list(json.loads(str(json_string)))

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes set
        Args:
            cls:
            dictionary: key word args list of a dictionary
        """
        if 'size' in dictionary:
            inst = cls(17)
        else:
            inst = cls(17, 12)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """ Returns the list of instances
            Args:
                cls: current class using this method
            Returns: the list of instances, empty list if file does not exist
        """
        file_name = cls.__name__ + '.json'
        if os.path.isfile(file_name):
            instList = []
            with open(file_name, 'r') as f:
                data = f.read()
                data = cls.from_json_string(data)
            for elem in data:
                instList.append(cls.create(**elem))
            return instList
        else:
            return []

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

        strData = []
        if list_objs is None:
            strData = '[]'
        else:
            objData = []
            for ob in list_objs:
                objData.append(ob.to_dictionary())
            #strData = cls.to_json_string(objData)
            #strData = 

        csv_file = cls.__name__ + ".csv"
        rect_fields = ['id', 'width', 'height', 'x', 'y']
        sqr_fields = ['id', 'size', 'x', 'y']
        with open(csv_file, mode="wt") as csvF:
            if cls.__name__ == 'Rectangle':
                writer = csv.DictWriter(csvF, fieldnames=rect_fields)
                writer.writeheader()
                for elem in objData:
                    writer.writerow(elem)
            else:
                writer = csv.DictWriter(csvF, fieldnames=sqr_fields)
                writer.writeheader()
                for elem in objData:
                    writer.writerow(elem)
    
    @classmethod
    def load_from_file_csv(cls):
        """ For deserializing a CSV file
        Args:
            cls:
        Returns: No return value?
        """
        file_name = cls.__name__ + '.csv'
        if os.path.isfile(file_name):
            instList = []
            with open(file_name, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                #data = cls.from_json_string(data)
                for row in reader:
                    '''objItem = {'id': row,
                            'width': row[1],
                            'height': row[2],
                            'x': row[3],
                            'y': rows[4]
                    }'''
                    instList.append(cls.create(**row))
                return instList
        else:
            return []


    def draw(list_rectangles, list_squares):
        """ Opens a window and prints all the rectagles and squares
        Args:
            list_rectangles: list of rectangles to print
            list_squares: list of squares to print
        Returns: No return value
        """
        turtle.pencolor('green')
        list
