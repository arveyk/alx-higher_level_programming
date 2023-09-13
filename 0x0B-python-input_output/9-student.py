#!/usr/bin/python3
"""Student class module
"""


class Student:
    """Student class defines a student with some characteristics
    """
    def __init__(self, fist_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves the JSON rep od a Student
        """
        import json
        return json.dumps(Student)
