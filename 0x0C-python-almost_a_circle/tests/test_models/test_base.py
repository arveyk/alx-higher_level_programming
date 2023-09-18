#!/usr/bin/prython3
""" Unittest Module """


import unittest
from models.base import Base

class TestBaseClass(Unittest.Testcase):

    def test_value(self):
        self.assertEqual(print(Base), Base.id)
        self.assertTrue()

if __name__ == '__main__':
    unittest.main()
