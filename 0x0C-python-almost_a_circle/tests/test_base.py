#!/usr/bin/python3
"""Unit tests for Base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    def test_base_id(self):
        """Test if Base assigns unique IDs"""
        base1 = Base()
        base2 = Base()
        base3 = Base(42)
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 42)

    def test_to_json_string(self):
        """Test the to_json_string method"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        expected_json = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]'
        self.assertEqual(json_string, expected_json)

    def test_from_json_string(self):
        """Test the from_json_string method"""
        json_string = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]'
        list_of_dicts = Base.from_json_string(json_string)
        self.assertEqual(list_of_dicts[0]['width'], 10)
        self.assertEqual(list_of_dicts[0]['x'], 2)
        self.assertEqual(list_of_dicts[0]['id'], 1)

    def test_save_to_file(self):
        """Test the save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            json_string = file.read()
            expected_json = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, {"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]'
            self.assertEqual(json_string, expected_json)
       

    def test_load_from_file(self):
        """Test the load_from_file method"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles[0].width, 10)
        self.assertEqual(rectangles[1].height, 4)

if __name__ == '__main__':
    unittest.main()
