#!/usr/bin/python3
"""
Solution to the lockboxes problem
"""

def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """

    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    n = len(boxes)
    unlocked = set([0])
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < n and key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])

    return len(unlocked) == n

