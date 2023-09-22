#!/usr/bin/python3
"""Defines a function inherits_from"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited.
    from the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
