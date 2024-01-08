#!/usr/bin/python3
"""
matrix_divided: a function to divide a matrix by div
"""


def matrix_divided(matrix, div):
    """
    matrix_divided: function to return a matrix divided by an integer
    Args:
        matrix: a list of integers or floats
        div: an integer or a float
    Raises:
         TypeError: exception with the message matrix must be a matrix
         (list of lists) of integers/floats
         TypeError: exception with the message Each row of the matrix must
         have the same size
         TypeError: exception with the message div must be a number
         ZeroDivisionError: exception with the message division by zero
    Returns:
        A new matrix with the divided values of matrix/div
    """

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        for column in row:
            if not (isinstance(column, int) or isinstance(column, float)):
                raise TypeError(
                    """matrix must be a matrix (list of lists) of
                     integers/floats"""
                )

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(column / div, 2) for column in row] for row in matrix]
    return new_matrix
