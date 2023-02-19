#!/usr/bin/python3
"""
Unittiest for Square([...])
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_raise_exception_for_str(self):
        with self.assertRaises(TypeError):
            s1 = Square("1", 2)
        with self.assertRaises(TypeError):
            s2 = Square(1, "2")
        with self.assertRaises(TypeError):
            s3 = Square(1, 2, "3")

    def test_raise_exception_for_0_or_neg(self):
        with self.assertRaises(ValueError):
            s1 = Square(-1, 2)
        with self.assertRaises(ValueError):
            s2 = Square(1, -2)
        with self.assertRaises(ValueError):
            s3 = Square(0, 2)

    def test_area(self):
        s = Square(2)
        self.assertEqual(s.area(), 4)

    def test_str(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")

    def test_to_dictionary(self):
        s = Square(1, 2, 3, 4)
        expected_output = {'x': 2, 'y': 3, 'id': 4, 'size': 1}
        self.assertEqual(s.to_dictionary(), expected_output)

    def test_update_no_args(self):
        s = Square(10, 20, 30, 50)
        s.update()
        self.assertEqual(str(s), "[Square] (50) 20/30 - 10")

    def test_update_1arg(self):
        s = Square(1, 0, 0, 1)
        s.update(2)
        self.assertEqual(str(s), "[Square] (2) 0/0 - 1")

    def test_update_2args(self):
        s = Square(1, 0, 0, 1)
        s.update(2, 2)
        self.assertEqual(str(s), "[Square] (2) 0/0 - 2")

    def test_update_3args(self):
        s = Square(1, 0, 0, 1)
        s.update(2, 2, 2)
        self.assertEqual(str(s), "[Square] (2) 2/0 - 2")

    def test_update_4_args(self):
        s = Square(1, 0, 0, 1)
        s.update(2, 2, 2, 2)
        self.assertEqual(str(s), "[Square] (2) 2/2 - 2")

    def test_update_id(self):
        s = Square(1)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_id_size(self):
        s = Square(1)
        s.update(**{'id': 89, 'size': 2})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)

    def test_update_id_width_height_x_y(self):
        s = Square(1)
        s.update(**{'id': 89, 'size': 1, 'x': 3, 'y': 4})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_create_id(self):
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

    def test_create_id_size_x(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 3})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 3)

    def test_create_id_size_x_y(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 3, 'y': 4})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_list(self):
        s = Square(2)
        Square.save_to_file([s])
