#!/usr/bin/python3
"""Class define lookup"""


def lookup(obj):
    """
    This function takes an object and returns a list of its attributes

    Args:
        obj(object): the object to inspect
    """
    return dir(obj)
