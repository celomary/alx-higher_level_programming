#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_idx in range(len(row)):
            print("{}".format(row[col_idx]), end='')
            print(end=" " if col_idx + 1 < len(row) else '\n')
