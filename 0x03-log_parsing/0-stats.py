#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys
import re


def printout(size: int, status_code: dict) -> None:
    """
    Function that displays stats
    """
    print(f'File size: {size}')
    for key, value in status_code.items():
        if value:
            print(f'{key}: {value}')


if __name__ == "__main__":
    count = 0
    status_code = {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
            }
    total_size = 0
    try:
        for line in sys.stdin:
            try:
                data = line.split(" ")
                stat_code = data[7]
                file_size = int(data[8])
                total_size += file_size
                status_code[stat_code] += 1
            except Exception:
                pass

            count += 1
            if (count % 10 == 0):
                printout(total_size, status_code)
    finally:
        printout(total_size, status_code)
