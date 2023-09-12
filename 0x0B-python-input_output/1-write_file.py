#!/usr/bin/python3
"""Defines a function write_file"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8)

    :param filename: The name of the file to write to.
    :param text: The text to write to the file.
    :return: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters


if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
