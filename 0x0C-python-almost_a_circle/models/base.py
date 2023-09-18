#!/usr/bin/python3
"""Base Module"""
import json

class Base:
    """Base class to manage IDs for other classes in the project."""

    __nb__objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
        id (int, optional): An integer ID for the instance. If provided, it will be assigned as the ID.
        If not provided, a new ID will be generated automatically.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (list): A list of dictionaries to be converted to JSON.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instanes to a JSON file.

        Args:
            list_objs (list): A list of instances to be saved to a JSON file.
        """
        filename = cls.__name__ + ".json"
        data = []

        if list_objs is not None:
            data = [obj.to_dictionary() for obj in list_objs]

        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(cls.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts JSON string to a list of dictionaries

        Args:
            json_string(str): A json string rep a list of dictionaries
        """

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create and return an instance with attribute set using a dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from)file(cls):
        """
        Load a list of instances from a JSON file

        Returns:
            list: a list of instances
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                data = file.read()
                dict_list = cls.from_json_string(data)
                return [cls.create(**d) for d in dict_list]
        except FileNotFoundError:
            return []
