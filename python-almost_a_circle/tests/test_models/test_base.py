#!/usr/bin/python3
"""
Unittiest for Base([...])
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_base_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_base_id_with_existing_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 3)
        b2 = Base()
        self.assertEqual(b2.id, 4)

    def test_base_given_id(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_to_json_str_w_None(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_str_w_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_str_w_list_of_dicts(self):
        self.assertEqual(Base.to_json_string([{ 'id': 12 }]), '[{"id": 12}]')

    def test_from_json_str_w_None(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_str_w_empty_str(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_str_w_lists_of_dicts(self):
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])

    if __name__ == "__main__":
        unittest.main()
