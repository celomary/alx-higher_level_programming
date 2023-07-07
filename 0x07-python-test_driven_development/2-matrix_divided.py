#!/usr/bin/python3

def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or any(
        [not isinstance(lst, list) for lst in matrix]
        ) or [not isinstance(number, (int, float))
              for number in
              [num for lst in matrix for num in lst]]:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(lst) for lst in matrix)) == 1:
        raise TypeError(
            "Each row of the matrix must have the same size")
    if div == 0:
        raise TypeError("div must be a number")
    return [[round(number, 2) for number in row]
            for row in matrix]
