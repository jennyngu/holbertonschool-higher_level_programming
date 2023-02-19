#!/usr/bin/python3
"""
Unittiest for Rectangle([...])
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    def test_rectangle_exists(self):
        r1 = Rectangle(1, 2)
        self.assertIsInstance(r1, Rectangle)
        r2 = Rectangle(1, 2, 3)
        self.assertIsInstance(r2, Rectangle)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(r3, Rectangle)
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r4, Rectangle)

    def test_raise_exception_for_str(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r2 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r3 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 2, 3, "4")

    def test_raise_exception_for_0_or_neg(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 2, 3, -4)
        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r6 = Rectangle(1, 0)

    def test_area(self):
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, "area"))

    def test_str(self):
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, "__str__"))

    def test_display(self):
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, "display"))

    def test_display_w_x_and_y_exists(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertTrue(hasattr(r, "display"))

    def test_display_wo_y_exists(self):
        r = Rectangle(1, 2, 3)
        self.assertTrue(hasattr(r, "display"))

    def test_to_dictionary(self):
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, "to_dictionary"))

    def test_update(self):
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, "update"))

    def test_create(self):
        self.assertTrue(hasattr(Rectangle, "create"))

    def test_save_to_file(self):
        self.assertTrue(hasattr(Rectangle, "save_to_file"))

    def test_load_from_file(self):
        self.assertTrue(hasattr(Rectangle, "load_from_file"))
