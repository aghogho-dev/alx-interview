#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Func"""
    n = len(matrix)
    for i in range(n // 2):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n - 1 - j)
            m = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            matrix[j][y] = m
