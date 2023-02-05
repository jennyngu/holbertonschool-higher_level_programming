#!/usr/bin/python3
"""
A function that divdes all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by the given number

    matrix: the matrix
    div: the number to divide elements by

    Return: new matrix with divided elements
    """
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError(matrix_error)
    if type(matrix[0]) != list:
        raise TypeError(matrix_error)
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    length = len(matrix[0])
    for row in matrix:
        if type(row) != list:
            raise TypeError(matrix_error)
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if type(element) != int and type(element) != float:
                raise TypeError(matrix_error)
            new_row.append(round(element/div, 2))
        new_matrix.append(new_row)
    return new_matrix
