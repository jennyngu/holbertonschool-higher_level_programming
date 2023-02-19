#!/usr/bin/python3
"""
Unittiest for Rectangle([...])
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(self):
    def test_rectangle_exists(self):
        r1 = Rectangle(1, 2)
        self.assertIsInstance(r1, Rectangle)
        r2 = Rectangle(1, 2, 3)
        self.assertIsInstance(r2, Rectangle)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(r3, Rectangle)
        r4 = Rectangle("1", 2)
        self.assertIsInstance(r4, Rectangle)
        r5 = Rectangle(1, "2")
        self.assertIsInstance(r5, Rectangle)
        r6 = Rectangle(1, 2, "3")
        self.assertIsInstance(r6, Rectangle)
        r7 = Rectangle(1, 2, 3, "4")
        self.assertIsInstance(r7, Rectangle)
        r8 = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r8, Rectangle)
        r9 = Rectangle(-1, 2)
        self.assertIsInstance(r9, Rectangle)
        r10 = Rectangle(1, -2)
        self.assertIsInstance(r10, Rectangle)
        r11 = Rectangle(0, 2)
        self.assertIsInstance(r11, Rectangle)
        r12 = Rectangle(1, 0)
        self.assertIsInstance(r12, Rectangle)
        r13 = Rectangle(1, 2, -3)
        self.assertIsInstance(r13, Rectangle)
        r14 = Rectangle(1, 2, 3, -4)
        self.assertIsInstance(r14, Rectangle)

    def test_area_exists(self):
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, "area"))

    def test_str_exists(self):
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, "__str__"))

    def test_display_exists(self):
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, "display"))

    def test_display_with_x_and_y_exists(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertTrue(hasattr(r, "display"))

    def test_display_without_y_exists(self):
        r = Rectangle(1, 2, 3)
        self.assertTrue(hasattr(r, "display"))

    def test_to_dictionary_exists(self):
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, "to_dictionary"))

    def test_update_exists(self):
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, "update"))

    def test_create_exists(self):
        self.assertTrue(hasattr(Rectangle, "create"))

    def test_save_to_file_exists(self):
        self.assertTrue(hasattr(Rectangle, "save_to_file"))

    def test_load_from_file_exists(self):
        self.assertTrue(hasattr(Rectangle, "load_from_file"))
