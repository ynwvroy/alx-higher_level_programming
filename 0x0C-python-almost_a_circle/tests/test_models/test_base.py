#!/usr/bin/python3
"""Edge case tests for Base class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_default_id_generation(self):
        """Test that Base class generates unique IDs starting from 1 by default"""
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id_assignment(self):
        """Test that Base class can accept a custom ID when provided"""
        b1 = Base(10)
        b2 = Base(20)
        b3 = Base(30)

        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 20)
        self.assertEqual(b3.id, 30)

    def test_mixed_id_assignment(self):
        """Test mixing custom and default IDs"""
        b1 = Base()
        b2 = Base(100)
        b3 = Base()
        b4 = Base(200)

        expected_ids = [1, 100, 2, 200]

        for i in range(len(expected_ids)):
            self.assertEqual(b1.id, expected_ids[i])
            b1 = Base()

    if __name__ == "__main__":
        unittest.main()
