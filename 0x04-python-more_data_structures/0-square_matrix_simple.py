#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result_matrix = []
    for row in matrix:
        squared_row = []
        for value in row:
            squared_row.append(value ** 2)
        result_matrix.append(squared_row)
    return result_matrix
