#!/usr/bin/python3
"""
Unit tests for the Base class.

Unittest classes:
    TestBaseInstantiation - line 21
    TestBaseToJsonString - line 108
    TestBaseSaveToFile - line 154
    TestBaseFromJsonString - line 232
    TestBaseCreate - line 286
    TestBaseLoadFromFile - line 338
    TestBaseSaveToFileCSV - line 404
    TestBaseLoadFromFileCSV - line 482
"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseInstantiation(unittest.TestCase):
    """Unit tests for testing instantiation of the Base class."""

    def test_no_arg(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    # Add more test cases for Base instantiation here

class TestBaseToJsonString(unittest.TestCase):
    """Unit tests for testing to_json_string method of Base class."""

    # Add test cases for to_json_string method here

class TestBaseSaveToFile(unittest.TestCase):
    """Unit tests for testing save_to_file method of Base class."""

    # Add test cases for save_to_file method here

class TestBaseFromJsonString(unittest.TestCase):
    """Unit tests for testing from_json_string method of Base class."""

    # Add test cases for from_json_string method here

class TestBaseCreate(unittest.TestCase):
    """Unit tests for testing create method of Base class."""

    # Add test cases for create method here

class TestBaseLoadFromFile(unittest.TestCase):
    """Unit tests for testing load_from_file method of Base class."""

    # Add test cases for load_from_file method here

class TestBaseSaveToFileCSV(unittest.TestCase):
    """Unit tests for testing save_to_file_csv method of Base class."""

    # Add test cases for save_to_file_csv method here

class TestBaseLoadFromFileCSV(unittest.TestCase):
    """Unit tests for testing load_from_file_csv method of Base class."""

    # Add test cases for load_from_file_csv method here

if __name__ == "__main__":
    unittest.main()
