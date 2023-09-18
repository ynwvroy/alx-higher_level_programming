#!/usr/bin/python3
"""Unit tests for Rectangle class"""

import unittest
import unittest.mock
import io
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle_attributes(self):
        """Test the attributes of the Rectangle class"""
        r = Rectangle(10, 20, 30, 40, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 1)

    def test_rectangle_area(self):
        """Test the area() method of the Rectangle class"""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_rectangle_display(self):
        """Test the display() method of the Rectangle class"""
        r = Rectangle(3, 2)
        expected_output = "###\n" \
                          "###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_rectangle_str(self):
        """Test the __str__() method of the Rectangle class"""
        r = Rectangle(5, 10, 15, 20, 25)
        self.assertEqual(str(r), "[Rectangle] (25) 15/20 - 5/10")

    def test_rectangle_update_args(self):
        """Test the update() method with positional arguments"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 2, 2, 2, 2)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")

    def test_rectangle_update_kwargs(self):
        """Test the update() method with keyword arguments"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(id=2, width=2, height=2, x=2, y=2)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")

    def test_rectangle_to_dictionary(self):
        """Test the to_dictionary() method of the Rectangle class"""
        r = Rectangle(5, 10, 15, 20, 25)
        expected_dict = {'id': 25, 'width': 5, 'height': 10, 'x': 15, 'y': 20}
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
