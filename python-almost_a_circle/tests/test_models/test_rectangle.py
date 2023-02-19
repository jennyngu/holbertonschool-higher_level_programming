#!/usr/bin/python3
"""
Unittiest for Rectangle([...])
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
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
        self.assertEqual(r.area(), 2)

    def test_str(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        expected_output = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertEqual(r.to_dictionary(), expected_output)

    def test_update_no_args(self):
        r = Rectangle(10, 20, 30, 40, 50)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (50) 30/40 - 10/20")

    def test_update_1arg(self):
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2)
        self.assertEqual(str(r), "[Rectangle] (2) 0/0 - 1/1")

    def test_update_2args(self):
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 2)
        self.assertEqual(str(r), "[Rectangle] (2) 0/0 - 2/1")

    def test_update_3args(self):
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 2, 2)
        self.assertEqual(str(r), "[Rectangle] (2) 0/0 - 2/2")

    def test_update_4_args(self):
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 2, 2, 2)
        self.assertEqual(str(r), "[Rectangle] (2) 2/0 - 2/2")

    def test_update_5args(self):
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 2, 2, 2, 2)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")

    def test_update_id(self):
        r = Rectangle(1, 1)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_update_id_width(self):
        r = Rectangle(1, 1)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_update_id_width_height(self):
        r = Rectangle(1, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_update_id_width_height_x(self):
        r = Rectangle(1, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_update_id_width_height_x_y(self):
        r = Rectangle(1, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_create_id(self):
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_create_id_width_height(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_create_id_width_height_x(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_create_id_width_height_x_y(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_list(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
