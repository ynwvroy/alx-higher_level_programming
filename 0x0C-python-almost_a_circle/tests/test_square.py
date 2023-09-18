import unittest
import json
import inspect

from models.square import Square
from unittest.mock import Mock


class TestSquare(unittest.TestCase):

    def test_square_init(self):
        # Test square initialization with valid arguments
        sq = Square(5, 1, 2, 10)
        self.assertEqual(sq.id, 10)
        self.assertEqual(sq.size, 5)
        self.assertEqual(sq.x, 1)
        self.assertEqual(sq.y, 2)

        # Test square initialization with default values
        sq = Square(5)
        self.assertEqual(sq.id, 1)
        self.assertEqual(sq.size, 5)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)

    def test_str_representation(self):
        sq = Square(5, 1, 2, 10)
        expected_str = "[Square] (10) 1/2 - 5"
        self.assertEqual(str(sq), expected_str)

    def test_size_property(self):
        sq = Square(5)
        sq.size = 10
        self.assertEqual(sq.size, 10)
        self.assertEqual(sq.width, 10)
        self.assertEqual(sq.height, 10)

    def test_update_method(self):
        sq = Square(5, 1, 2, 10)
        sq.update(20, 7, 8, 15)
        self.assertEqual(sq.id, 20)
        self.assertEqual(sq.size, 7)
        self.assertEqual(sq.x, 8)
        self.assertEqual(sq.y, 15)

        sq.update(x=3, y=4)
        self.assertEqual(sq.x, 3)
        self.assertEqual(sq.y, 4)

    def test_to_dictionary_method(self):
        sq = Square(5, 1, 2, 10)
        sq_dict = sq.to_dictionary()
        expected_dict = {'id': 10, 'size': 5, 'x': 1, 'y': 2}
        self.assertEqual(sq_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
