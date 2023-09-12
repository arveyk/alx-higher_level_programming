#!/usr/bin/python3
"""In this BaseGeometry, the area method is implemented

"""


class BaseGeometry():
    """Computes area based on mesurement given
    """

    def area(self):
        """Raises an exception indicating the area method has not been
            implemented
            Args: no args
            Returns: no return value
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates(checks) if value is an integer
        raises an exception message if it isn't
            Args:
                name: the name for the dimension
                value: the value for the dimension
            Returns: No return value
        """
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
        self.name = name
        self.value = value
