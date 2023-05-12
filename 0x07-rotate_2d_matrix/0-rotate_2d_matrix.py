#!/usr/bin/python3

"""
Rotating a two-dimensional matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for l in range(i, matrix_length):
            matrix[i][l], matrix[l][i] = matrix[l][i], matrix[i][l]

    for i in range(matrix_length):
        matrix[i] = matrix[i][::-1]