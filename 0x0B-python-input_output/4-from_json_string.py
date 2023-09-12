#!/usr/bin/python3
"""
Returns object represented by the JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns object represented by a JSON string
    """
    return json.loads(my_str)
