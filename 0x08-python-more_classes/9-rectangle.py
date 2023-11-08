#!/usr/bin/python3
"""Class Rectangle that computes the area and perimeter of a tringle
    of given dimensions
"""


class Rectangle:
    """Rectangle class defines a rectangle of a certain height and width which
    are >= 0
    Args:
        number_of_instances: counts number of triangles created
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize every intatance object
            Args:
                width: the width of the rectagle
                height: the Height of the rectangle
            Returns: no return value
        """
        Rectangle.number_of_instances += 1
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
        self.__width = width

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        hgt = self.__height
        while hgt > 0:
            for wdth in range(self.__width):
                print('{}'.format(self.print_symbol), end="")
            if hgt > 1:
                print()
            hgt -= 1
        return ''

    def __repr__(self):
        """Returns the 'formal' representation of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        return f'Rectangle({self.__width}, {self.__height})'

    @property
    def width(self):
        """Getter: retrives the class attribute
            Setter: mutates the attributes"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter: gets the height attribute
            Returns: the height
            Setter: changes the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """calculates the area of a rectangle
            Args:
                None
            Returns: the area computed
            """
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of a rectangle
            Args:
                None
            Returns: the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two class instances
            Args:
                rect_1: first class att
                rect_2: second class att
            Returns: rect_1 if rect_1 is equal to rect_2
        """
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 == area_2:
            return rect_1
        if area_1 > area_2:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """defines a Square
        Args:
            size: the dimensions of the square
        Return:
            the Square class
        """
        return cls(size, size)
