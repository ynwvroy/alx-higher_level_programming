import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """A unittest class for testing the Square class."""

    def setUp(self):
        """Set up a Square instance for testing."""
        self.square = Square(3)

    def test_attributes(self):
        """Test if the attributes of the Square instance are set correctly."""
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.width, 5)
        self.assertEqual(self.square.height, 5)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)
        self.assertEqual(self.square.id, 1)

    def test_str(self):
        """Test the string representation of the Square."""
        expected_str = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(self.square), expected_str)

    def test_update(self):
        """Test the update method of the Square."""
        self.square.update(2, 4, 6, 8, id=3)
        self.assertEqual(self.square.id, 2)
        self.assertEqual(self.square.size, 4)
        self.assertEqual(self.square.x, 6)
        self.assertEqual(self.square.y, 8)

    def test_to_dictionary(self):
        """Test the to_dictionary method of the Square."""
        expected_dict = {
            'id': 1,
            'size': 5,
            'x': 2,
            'y': 3
        }
        self.assertEqual(self.square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
