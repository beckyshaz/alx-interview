#!/usr/bin/python3
"""Determining the number of minimal operations to be
taken to carryout copyall and paste using python"""


def minOperations(n):
    """using python to determine the number of minimal
    operations to be carried out"""

    if n <= 0:
        return 0
    num_items = 1
    num_operations = 0
    num_copied_items = 0

    while (num_items < n):
        if n % num_items == 0:
            num_operations += 2
            num_copied_items = num_items
            num_items += num_copied_items
        else:
            num_operations += 1
            num_items += num_copied_items
    return num_operations
