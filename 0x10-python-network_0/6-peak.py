#!/usr/bin/python3
"""
find the peek
"""


def find_peak(arr):
    """
        find the peek
    """

    if arr is None or len(arr) == 0:
        return None
    if len(arr) == 1:
        return max(arr)

    prev = arr[0]

    for i in range(1, len(arr) - 1):
        if arr[i] > prev and arr[i + 1] < arr[i]:
            return arr[i]
        prev = arr[i]
    return max(arr)
