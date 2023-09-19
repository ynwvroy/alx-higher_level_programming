#!/usr/bin/python3
import unittest
import json
from models.base import Base

class TestBase(unittest.TestCase):
    """
    A unittest class for testing the Base class and its methods.
    """

    def setUp(self):
        """
        Set up a Base instance for testing.
        """
        self.instances = Base()

    def tearDown(self):
        """
        Clean up after each test.
        """
        Base._Base__nb_objects = 0  # Reset the __nb_objects counter to 0

    def test_init(self):
        """
        Test the constructor (__init__) of the Base class.
        """
        self.assertEqual(self.base_instance.id, 1)
        new_base_instance = Base(100)
        self.assertEqual(new_base_instance.id, 100)

    def test_to_json_string(self):
        """
        Test the to_json_string method of the Base class.
        """
        dict_list = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_string = Base.to_json_string(dict_list)
        self.assertEqual(json_string, json.dumps(dict_list))

    def test_save_to_file(self):
        """
        Test the save_to_file method of the Base class.
        """
        dict_list = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        isinstances = [Base.create(**d) for d in dict_list]
        Base.save_to_file([self.base_instance])
        with open("Base.json", mode="r", encoding="utf-8") as file:
            saved_json_string = file.read()
        self.assertEqual(saved_json_string, Base.to_json_string([obj.to_dictionary() for obj in instances]))

    def test_from_json_string(self):
        """
        Test the from_json_string method of the Base class.
        """
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        dict_list = Base.from_json_string(json_string)
        self.assertEqual(dict_list, json.loads(json_string))

    def test_create(self):
        """
        Test the create method of the Base class.
        """
        dictionary = {'id': 3, 'name': 'Charlie'}
        instance = Base.create(**dictionary)
        self.assertEqual(instance.id, 3)
        self.assertEqual(instance.__class__.__name__, "Base")

    def test_load_from_file(self):
        """
        Test the load_from_file method of the Base class.
        """
        dict_list = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        isinstances = [Base.create(**d) for d in dict_list]
        Base.save_to_file(instances)
        loaded_instances = Base.load_from_file()
        self.assertEqual(len(loaded_instances), 2)
        self.assertEqual(loaded_instances[0].id, 1)
        self.assertEqual(loaded_instances[1].id, 2)

if __name__ == '__main__':
    unittest.main()
