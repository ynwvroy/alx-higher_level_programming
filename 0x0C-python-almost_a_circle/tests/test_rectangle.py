import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    A unittest class for testing the Rectangle class.
    """

    def setUp(self):
        """
        Set up a Rectangle instance for testing.
        """
        self.rectangle = Rectangle(2, 4)

    def test_attributes(self):
        """
        Test if the attributes of the Rectangle instance are set correctly.
        """
        self.assertEqual(self.rectangle.width, 4)
        self.assertEqual(self.rectangle.height, 5)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 3)
        self.assertEqual(self.rectangle.id, 1)

    def test_area(self):
        """
        Test the area method of the Rectangle.
        """
        self.assertEqual(self.rectangle.area(), 20)

    def test_display(self):
        """
        Test the display method of the Rectangle.
        """
        r1 = Rectangle(4, 5, 2, 2)
        expected_output = "####\n####\n####\n####\n####"
        self.assertEqual(r1.display(), expected_output)

    def test_str(self):
        """
        Test the string representation of the Rectangle.
        """
        expected_str = "[Rectangle] (1) 2/3 - 4/5"
        self.assertEqual(str(self.rectangle), expected_str)

    def test_update(self):
        """
        Test the update method of the Rectangle.
        """
        self.rectangle.update(2, 6, 7, 8, 9, id=10)
        self.assertEqual(self.rectangle.id, 2)
        self.assertEqual(self.rectangle.width, 6)
        self.assertEqual(self.rectangle.height, 7)
        self.assertEqual(self.rectangle.x, 8)
        self.assertEqual(self.rectangle.y, 9)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method of the Rectangle.
        """
        expected_dict = {
            'id': 1,
            'width': 4,
            'height': 5,
            'x': 2,
            'y': 3
        }
        self.assertEqual(self.rectangle.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
