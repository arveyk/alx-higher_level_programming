#!/usr/bin/python3
"""Square module """


from models.rectangle import Rectangle

class Square(Rectangle):
    """ Defines a square, similar to a rectangle but 
        with width == height
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(self.width, self.height)
