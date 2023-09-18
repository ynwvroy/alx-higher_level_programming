#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_negative_width(self):
        """Test if width is negative"""
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    def test_negative_height(self):
        """Test if height is negative"""
        with self.assertRaises(ValueError):
            r = Rectangle(2, -1)

    def test_negative_x(self):
        """Test if x is negative"""
        with self.assertRaises(ValuError):
            r = Rectangle(2, 2, -1)

    def test_negative_y(self):
        """Test if y is negative"""
        with self.assertRaises(ValueError):
            r = Rectangle(2, 2, 1, -1)

    def test_non_integer_width(self):
        """Test if width is not an integer"""
        with self.assertRaises(TypeError):
            r = Rectangle("2", 2)

    def test_non_integer_height(self):
        """Test if height is not an integer"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, "2")

    def test_non_integer_x(self):
        """Test if x is not an integer"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, "1")

    def test_non_integer_y(self):
        """Test if y is not an integer"""
        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, 1, "1")

    def test_zero_width(self):
        """Test if width is zero"""
        with self.asserRaises(ValueError):
            r = Rectangle(0, 2)

    def test_zero_height(self):
        """Test if height is zero"""
        with self.assertRaises(ValueError):
            r = Rectangle(2, 0)

    def test_zero_x(self):
        """Test if x is zero"""
        r = Rectangle(2, 2, 0)
        self.assertEqual(r.x, 0)

    def test_zero_y(self):
        """Test if y is zero"""
        r = Rectangle(2, 2, 1, 0)
        self.assertEqual(r.y, 0)

if __name__ == "__main__":
    unittest.main()
