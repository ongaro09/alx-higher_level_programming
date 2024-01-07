#!/usr/bin/python3
"""
This module provides a function `matrix_divided` that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and rounds the result to 2 decimal places.

    Args:
        matrix (list of lists of ints/floats): The matrix to be divided.
        div (int/float): The divisor to divide the matrix by.

    Returns:
        list: A new matrix with all elements divided by div.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats, if each row of
                   the matrix is not the same size, or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]

