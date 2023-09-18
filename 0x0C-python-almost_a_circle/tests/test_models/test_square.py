import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_constructor(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_str(self):
        s = Square(5, 2, 3, 7)
        self.assertEqual(str(s), "[Square] (7) 2/3 - 5")

    def test_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_display(self):
        s = Square(3, 2, 1)
        expected_output = " " * 2 + "##\n" + " " * 2 + "##\n" + " " * 2 + "##\n"
        self.assertEqual(s.display(), expected_output)

    def test_update(self):
        s = Square(3)
        s.update(1, 2, 3, 4, 5)
        self.assertEqual(s.__str__(), "[Square] (1) 4/5 - 2")

if __name__ == "__main__":
    unittest.main()
