#!/usr/bin/python3
""" Module for Rectangle class definition """

from models.base import Base


class Rectangle(Base):
    """ Defines a Rectangle, inherits from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Why the init method
            Args:
                width: width of rect
                height: height
                x: x
                y: y
                id: identification
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        getter:gets the dimention and validates
        setter: sets it
        """

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
        """
        getter:gets the dimention and validates
        setter: sets it
        """
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
        """
        getter:gets the dimention and validates
        setter: sets it
        """
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """
        getter:gets the dimention and validates
        setter: sets it
        """
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """ area fuctions calculates the area of a rectangle
            Args: No args
            Returns: area computed
        """
        return self.__width * self.__height

    def display(self):
        """ prints out the rectangle width units wide and height units
            high
            Args: None
            Returns: no return value
        """
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
        """ Returns the string representation of Rectangle class
        Args: Self only
        Returns: informal str representation
        """
        cls_nm = (Rectangle.__name__)
        string1 = f'[{cls_nm}] ({self.id}) {self.x}'
        string2 = f'/{self.y} - {self.width}/{self.height}'
        return (string1 + string2)

    def update(self, *args, **kwargs):
        """ updates dimensions of rectangle
            Args:
                *args: access unknown number of arguments
                **kwargs: access a key, value dictionary varied
                number of argument
            Returns: No explicit return value
        """
        if kwargs is not None and (args is None or len(args) == 0):
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
        else:
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
    
    def to_dictionary(self):
        """ Returns the dictionary representation of a rectangle
            Args: None
            Return: dictionary representation of a rectangle
        """
        rect_dict_rep = {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
        return rect_dict_rep
