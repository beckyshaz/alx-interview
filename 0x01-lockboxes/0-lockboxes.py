#!/usr/bin/python3
"""Checking if a key in a certain box can unlock
locked boxes using python algorithm"""


def canUnlockAll(boxes):
    """checking if a box has a key to unlock a
    locked box"""

    if (type(boxes) != list and len(boxes) == 0):
        return False

    keyAvailable = [0]
    usedKeys = set()
    lenBoxes = len(boxes)

    while keyAvailable:
        boxIndex = keyAvailable.pop()
        usedKeys.add(boxIndex)
        openedBox = boxes[boxIndex]

        if type(openedBox) != list:
            return False
        for key in openedBox:
            if (
                    (key < lenBoxes) and
                    (key not in keyAvailable) and
                    (key not in usedKeys)):
                keyAvailable.append(key)
    return len(usedKeys) == lenBoxes
