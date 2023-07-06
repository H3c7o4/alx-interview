#!/usr/bin/python3
"""

This module contains the solution of the lockboxes problem

"""


def canUnlockAll(boxes):
    """

    Args:
      boxes: List of lists

    Returns:
        True if all boxes can be open, otherwise false.

    """
    visited = [False] * len(boxes)
    visited[0] = True

    keys = [0]

    while keys:
        current_key = keys.pop()
        current_box = boxes[current_key]

        for key in current_box:
            if not visited[key]:
                keys.append(key)
                visited[key] = True

    return all(visited)
