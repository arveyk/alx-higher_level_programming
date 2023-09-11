#!/usr/bin/python3
"""inverted Rebel child class
"""


class MyInt(int):
    """inherits from int class
    inverts ==  and != opertators
    """
    def __init__(self, other):
        def __eq__(self, other):
            return (self.a != other.b)
        def __ne__(self, other):
            return self.a == other.a
