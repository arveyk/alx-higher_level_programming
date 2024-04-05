#!/usr/bin/python3
"""Square module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a square, similar to a rectangle but
        with width == height
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        return f'[{Square.__name__}] {self.id} {self.x}/{self.y} - {self.size}'

    @property
    def size(self):
        """Getter: returns the size attribute
        Setter: modifies the value of the size attribut
        """
        return self.__size

    @size.setter
    def size(self, size):
        self.__width = size
        self.__height = size
