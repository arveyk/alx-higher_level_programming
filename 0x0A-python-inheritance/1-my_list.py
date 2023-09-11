#!/usr/bin/python3
"""Module to demo inheriring from list
"""

class MyList(list):
    """Inerits from list
    """
    def print_sorted(self):
        """Prints the inhertited sorted list
        """
        print(list.sort)
