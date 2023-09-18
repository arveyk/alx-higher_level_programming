#!/usr/bin/python3
""" Unittest Module for Square class """

import unittest
from module.square import Square


class TestSquare(unittest.Testcase):
    def test_type():
        self.assertRaises(ZeroDivisionError, Square, 0)
        self.assertRaises(ValueError, Square, -9)
    def test_value():
        self.assertEqual(Square.area(6), 36)
        self.assertRaises(TypeError, Square.perimeter, "65")
        self.assertRaises(TypeError, Square, [1, 2, 3, 4])
        self.assertRaises(TypeError, Square, {1, 3, 4, 7})

if __name__ == '__main__':
    unittest.main()
