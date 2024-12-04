#!/usr/bin/python3
"""Square module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a square, similar to a rectangle but
        with width == height
    """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        name = Square.__name__
        return f'[{name}] ({self.id}) {self.x}/{self.y} - {self.size}'

    @property
    def size(self):
        """Getter: returns the size attribute
        Setter: modifies the value of the size attribut
        """
        '''
        if self.size is not None:
            if type(size) is int:
                return self.size
                '''
        return self.__width

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('width must be an integer')
        if size <= 0:
            raise ValueError('width must be > 0')
        self.__width = size
        self.__height = size

    def update(self, *args, **kwargs):
        """Updates/ assigns attributes
        Args:
            args: holds a list of values
            kwargs: holds a list of key value pairs
        Returns: No return Value
        """
        if args:
            args_list = [0, 0, 0, -1, -1]
            p = 0
            for ar_g in args:
                if ar_g is not None:
                    args_list[p] = ar_g
                p += 1

            if (args_list[0] != 0):
                self.id = args_list[0]
            if (args_list[1] != 0):
                self.__width = args_list[1]
            if (args_list[2] != 0):
                self.__height = args_list[2]
            if (args_list[3] >= 0):
                self.__x = args_list[3]
            if (args_list[4] >= 0):
                self.__y = args_list[4]
        elif kwargs is not None and (args is None or len(args) == 0):
            kw_list = [0, 0, 0, -1, -1]
            kw_str = ["id", "width", "height", "x", "y"]

            for key, value in kwargs.items():
                k = 0
                while k < 5:
                    if value is not None:
                        if kw_str[k]:
                            if kw_str[k] == str(key) and k == 0:
                                self.id = value
                            elif kw_str[k] == str(key) and k == 1:
                                self.__width = value
                            elif kw_str[k] == str(key) and k == 2:
                                self.__height = value
                            elif kw_str[k] == str(key) and k == 3:
                                self.__x = value
                            elif kw_str[k] == str(key) and k == 4:
                                self.__y = value
                    k += 1

    def to_dictionary(self):
        """ Returns the dictionary representation of a square
            Args: None
            Return: dictionary representation of a square
        """
        sqr_dict_rep = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
        return sqr_dict_rep
