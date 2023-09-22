#!/usr/bin/python3
"""defines the function is_same_class"""


def is_same_class(obj, a_class):
    """
    check if an object is exactly an instant of the specified class

    Args:
        abj (object): the object to check
        a_class: the class to compare against
    """
    return type(obj) is a_class
