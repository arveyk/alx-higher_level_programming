#!/usr/bin/python3
""" Unittest module for Rectangle """

import unittest
from module.rectangle import Rectangle


class TestRectangle(unittest.Testcase):
    def test_type():
        self.assertRaises(ZeroDivisionError, Rectangle, 0)
        self.assertRaises(ValueError, Rectangle, -9)
    def test_value():
        self.assertEqual(Rectangle.area(6), 36)
        self.assertRaises(TypeError, Rectangle.perimeter, "65")
        self.assertRaises(TypeError, Rectangle, [1, 2, 3, 4])
        self.assertRaises(TypeError, Rectangle, {1, 3, 4, 7})

if __name__ == '__main__':
    unittest.main()
