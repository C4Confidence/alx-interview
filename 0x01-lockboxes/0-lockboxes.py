#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    opened = [False] * n
    opened[0] = True  # The first box is always unlocked
    keys = set(boxes[0])  # Start with keys from the first box

    while keys:
        new_keys = set()
        for key in keys:
            if key < n and not opened[key]:
                opened[key] = True
                new_keys.update(boxes[key])
        keys = new_keys

    return all(opened)
