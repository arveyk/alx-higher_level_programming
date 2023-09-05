#!/usr/bin/python3
def print_square(size):
    """prints a 2 * 2 grid"""

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')

    for g in range(size):
        for z in range(size):
          print('#', end='')
        print()
