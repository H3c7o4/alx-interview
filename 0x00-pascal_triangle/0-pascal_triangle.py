#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    :type n: int
    :return type: int
    """
    mat = list(range(n))
    mat[0] = [1]
    mat[1] = [1, 1]

    if n <= 0:
        return []
    if n == 1:
        return mat[0]
    if n == 2:
        return mat[1]
    if n > 2:
        for i in range(2, n):
            mat[i] = [
                mat[i - 1][j] + mat[i - 1][j + 1]
                for j in range(len(mat[i - 1]) - 1)
            ]
            mat[i] = [1] + mat[i] + [1]
        return mat
