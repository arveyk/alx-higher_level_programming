#!/usr/bin/python3
""" Module for Rectangle class definition """

from models.base import Base


class Rectangle(Base):
    """ Defines a Rectangle, inherits from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be > 0')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be > 0')
        self.__y = y

    def area(self):
        """ Calculates the area of a triangle
            Args: None
            Returns: area calculated
        """
        return self.__width * self.__height

    def display(self):
        for d in range(self.y):
            print()
        for a in range(self.__height):
            if a > 0:
                print()
            for x in range(self.x):
                print(" ", end="")
            for b in range(self.__width):
                print('#', end="")
        print()

    def __str__(self):
        cls_nm = (Rectangle.__name__)
        string1 = f'[{cls_nm}] ({self.id}) {self.x}'
        string2 = f'/{self.y} - {self.width}/{self.height}'
        return (string1 + string2)
    
    def update(self, *args, **kwargs):
        
        p = 0
        arg0, arg1, arg2, arg3, arg4 = 0, 0, 0, 0, 0
        args_list = [arg0, arg1, arg2, arg3, arg4]
        
        if args is None and kwargs is not None:
            alld_keys = {"id", "width", "height", "x", "y"}

            '''self.__dict__.update((key, value) for key, value in kwargs.items() if key in alld_keys)'''
            for k, v in kwargs.items():
                setattr(self, k, v)

        else:
            for ar_g in args:
                args_list[p] = ar_g
                p += 1
            
            if args_list[0] != 0:
                self.id = args_list[0]
            if args_list[1] != 0:
                self.__width = args_list[1]
            if args_list[2] != 0:
                self.__height = args_list[2]
            if args_list[3] != 0:
                self.__x = args_list[3]
            if args_list[4] != 0:
                self.__y = args_list[4]
