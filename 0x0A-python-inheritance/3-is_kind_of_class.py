#!/usr/bin/python3
"""Defines a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    check if an object is an instance of.

    Args:
    obj (object): the object to check
    a_class: the class to compare against
    """

    return isinstance(obj, a_class)
