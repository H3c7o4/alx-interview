#!/usr/bin/python3
"""
Function to rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """

    Args:
      - matrix(List): A list of list to rotate

    Returns:
      - None
    """
    n = len(matrix)
    temp = matrix[::-1]

    for i in range(n):
        matrix[i] = []
        for j in range(n):
            matrix[i].append(temp[j].pop(0))
