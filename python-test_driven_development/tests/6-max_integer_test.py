#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        #Short ordered list
        self.assertEqual(max_integer([1, 2, 3]), 3)
        #Long ordered list
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
        #Short unordered list
        self.assertEqual(max_integer([2, 3, 1]), 3)
        #Long unordered list
        self.assertEqual(max_integer([1, 2, 4, 7, 5, 6, 9, 10, 8]), 10)
        #Ordered list with floats
        self.assertEqual(max_integer([1.3, 2.8, 6.8, 6.2]), 6.8)
        #Empty list
        self.assertIsNone(max_integer([]))
        #No list
        self.assertEqual(max_integer(), None)
        #List with duplicates
        self.assertEqual(max_integer([1, 4, 8, 8, 6]), 8)
        #List with negative values
        self.assertEqual(max_integer([-5, -1, 2, 3]), 3)

if __name__ == '__main__':
    unittest.main()
