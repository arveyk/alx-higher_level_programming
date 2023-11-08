#!/usr/bin/python3
"""Module that defines Student class
"""


class Student:
    """
    Defines a student with first name, last name and age credentials
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the class attribute on every object or instance
        of the class
            Args:
                first_name: 1st name of the student
                last_name: 2nd identifier for the student
                age: the numerical count of number of yrs lived
                    by the student
            Returns: No return value
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """return dictionary for JSON serialization of an object
        Args:
            obj: the class object
        Returns: the dictionary description
        """
        new_dict = {}
        if type(attr) is list:
            for name in attr:
                if name in self.__dict__:
                    new_dict[name] = self.__dict__[name]
            return (new_dict)
        else:
            return dict(self.__dict__)

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        Args:
            json - dictionary
        Returns: None yet
        """
        new_dict = self.__dict__ = json
