#!/usr/bin/python3
"""Base module"""
import json


class Base:
    """Base class to manage IDs for other classes in the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int, optional): An integer ID for the instance............
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a JSON file.

        Args:
            list_objs (list): A list of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string rep.

        Returns:
            list: A list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set.

        Args:
            dictionary (dict): A dictionary of attributes and their values.

        Returns:
            Base: An instance with the attributes set.
        """
        if cls.__name__ == "Base":
            dummy = cls()
        else:
            dummy = cls(1)  # Use 1 as a default ID for subclasses
        dummy.update(**dictionary)
        return dummy

    def update(self, *args, **kwargs):
        """
        Update instance attribute based on arguments

        Args:
            *args: variable length
            **kwargs: keyword
        """
        if args:
            attr_names = ['id']
            for arg in args:
                for key, value in arg.items():
                    setattr(self, key, value)
                    if key not in attr_names:
                        attr_names.append(key)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """converts instance attributes to a dict"""
        return {key: getattr(self, key) for key in vars(self)}

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_data = file.read()
                dict_list = cls.from_json_string(json_data)
                return [cls.create(**d) for d in dict_list]
        except FileNotFoundError:
            return []
