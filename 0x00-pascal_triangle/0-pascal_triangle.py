#!/usr/bin/python3
"""implementing pascal triangle using python algorithm"""


def pascal_triangle(n):
    """pascal triangle using loops in python"""
    if (n <= 0):
        return []
    triangle = []
    for index in range(n):
        rows = []
        for i in range(index + 1):
            if (i == 0) or (i == index):
                rows.append(1)
            else:
                rows.append(
                    triangle[index - 1][i] + triangle[index - 1][i - 1]
                    )
        triangle.append(rows)
    return triangle
