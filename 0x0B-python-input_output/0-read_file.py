#!/usr/bin/python3
"""defines a read_file function"""


def read_file(filename=""):
    """
    Read the content of a text file and print it to stdout.

    :param filename: The name of the file to read (UTF8 encoded).
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')


if __name__ == "__main__":
    read_file("my_file_0.txt")
