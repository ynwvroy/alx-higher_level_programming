#!/usr/bin/python3
"""Defines a function append_write"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF8)

    :param filename: The name of the file to append to.
    :param text: The text to append to the file.
    :return: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        nb_characters_added = file.write(text)
    return nb_characters_added


if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
    print(nb_characters_added)
