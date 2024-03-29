#!/usr/bin/python3
"""Unittest for max_interger([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unit test class
    """

    def test_exception(self):
        """Checks for exceptions raised
        """
        self.assertRaises(TypeError, max_integer, [1, 'e', 7])
        self.assertRaises(TypeError, max_integer, [1 + 8j, 2, 8])

    def test_max(self):
        """Checks for maximum value
        """
        self.assertEqual(max_integer([-8, 3, 10, 76]), 76)
        self.assertEqual(max_integer([64, 2, 3, 4]), 64)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([1, 2, 59, 3]), 59)
        self.assertEqual(max_integer([-1, -2, -4, -3]), -1)
