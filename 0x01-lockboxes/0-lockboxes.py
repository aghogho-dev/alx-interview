#!/usr/bin/python3
"""Lockboxes module"""


def canUnlockAll(boxes):
    """
    Args:
      boxes
    Return: bool
    """
    keys = set([0])
    while True:
        prev_len = len(keys)
        for i in range(len(boxes)):
            if i in keys:
                keys.update(boxes[i])
        if len(keys) == prev_len:
            break
    return len(keys) == len(boxes)
