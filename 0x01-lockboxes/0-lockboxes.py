#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened."""
    if len(boxes) == 0:
        return False
    if type(boxes) is not list:
        return False
    if len(boxes) == 1:
        return True
    visited = [0]
    for current_box in visited:
        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                visited.append(key)
    if len(visited) == len(boxes):
        return True
    return False
