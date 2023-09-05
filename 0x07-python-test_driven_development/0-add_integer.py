#!/usr/bin/python3
def add_integer(a, b=98):

    """Funtion that adds to integers"""
    """if type(a) is not int or type(a) is not float:
        raise TypeError('a must be an integer or b must be an integer')
    if type(b) is not int or type(b) is not float:
        raise TypeError('a must be an integer or b must be an integer')
        """
    result = 0
    try:
        result += int(b)
        try:
            result += int(a)
        except TypeError:
            print('a must be an integer')
    except TypeError:
        print('b must be an integer')
    return result
