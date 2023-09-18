#!/usr/bin/python3
"""Unit tests for Square class"""

import unittest
import unittest.mock
import io
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_square_attributes(self):
        """Test the attributes of the Square class"""
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 1)

    def test_square_area(self):
        """Test the area() method of the Square class"""
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.area(), 25)

    def test_square_display(self):
       """Test the display() method of the Square class"""
        s = Square(3, 1, 1)
        expected_output = ' ###\n ###\n ###\n'  # Remove the leading newline character
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output

    def test_square_str(self):
        """Test the __str__() method of the Square class"""
        s = Square(5, 2, 3, 1)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 5")

    def test_square_update_args(self):
        """Test the update() method with positional arguments"""
        s = Square(5, 2, 3, 1)
        s.update(2, 4, 5, 6)
        self.assertEqual(str(s), "[Square] (2) 5/6 - 4")

    def test_square_update_kwargs(self):
        """Test the update() method with keyword arguments"""
        s = Square(5, 2, 3, 1)
        s.update(id=2, size=4, x=5, y=6)
        self.assertEqual(str(s), "[Square] (2) 5/6 - 4")

    def test_square_to_dictionary(self):
        """Test the to_dictionary() method of the Square class"""
        s = Square(5, 2, 3, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
