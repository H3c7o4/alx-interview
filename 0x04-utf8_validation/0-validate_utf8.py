#!/usr/bin/python3
"""
UTF-8 Validation
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """

    Args:
       data(List): data setrepresented by a list of integers

    Returns:
        True if data is a valid UTF-8 encoding, else return False
    """
    i = 0
    n = len(data)
    data_b = [bin(elt).replace('0b', '') for elt in data]

    while (i < n):
        nb = len(data_b[i])

        if nb < 8:
            i += 1
            continue

        dt = data_b[i][-8:]

        if dt[0:3] == '100':
            return False
        elif dt[0:3] == '110':
            dt_p1 = data_b[i + 1][-8:]
            if dt_p1[0:2] == '10':
                i += 2
                continue
            return False
        elif dt[0:4] == '1110':
            dt_p1 = data_b[i + 1][-8:]
            dt_p2 = data_b[i + 2][-8:]
            if dt_p1[0:2] == '10' and dt_p2[0:2] == '10':
                i += 3
                continue
            return False
        elif dt[0:6] == '11110':
            dt_p1 = data_b[i + 1][-8:]
            dt_p2 = data_b[i + 2][-8:]
            dt_p3 = data_b[i + 3][-8:]
            if (dt_p1[0:2] == '10'
                    and dt_p2[0:2] == '10'
                    and dt_p3[0:2] == '10'):
                i += 4
                continue
    return True
