#!/usr/bin/python3
"""Defines the function pascal triangle"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    :param n: The number of rows to generate.
    :return: A list of lists representing Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            previous_row = triangle[i - 1]
            new_row = [1]
            for j in range(1, i):
                new_value = previous_row[j - 1] + previous_row[j]
                new_row.append(new_value)
            new_row.append(1)
            triangle.append(new_row)

    return triangle


def print_triangle(triangle):
    """
    Print the Pascal's triangle.

    :param triangle: A list of lists representing Pascal's triangle.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
