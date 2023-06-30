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

    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    mat[0] = [1]
    mat[1] = [1, 1]
    if n > 2:
        for i in range(2, n):
            mat[i] = [
                mat[i - 1][j] + mat[i - 1][j + 1]
                for j in range(len(mat[i - 1]) - 1)
            ]
            mat[i] = [1] + mat[i] + [1]
        return mat
