#!/usr/bin/python3
"""
writes an object to the text file using JSON
"""
inport json


def save_to_json_file(my_obj, filename):
    """
    writes object to text files
    """
    with open(filename, 'w', encoding='utf-8') as f:
        cont = json.dumps(my_obj)
        f.write(cont)
