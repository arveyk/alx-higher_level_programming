#!/usr/bin/python3
"""Square module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a square, similar to a rectangle but
        with width == height
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        # self.__size = size

    def __str__(self):
        name = Square.__name__
        return f'[{name}] ({self.id}) {self.x}/{self.y} - {self.size}'

    @property
    def size(self):
        """Getter: returns the size attribute
        Setter: modifies the value of the size attribut
        """
        return self.width

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('width must be an integer')
        if size <= 0:
            raise ValueError('width must be > 0')
        self.__width = size
        self.__height = size
