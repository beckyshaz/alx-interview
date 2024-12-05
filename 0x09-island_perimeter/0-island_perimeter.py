#!/usr/bin/python3
"""this is to find the perimeter of an island"""


grids = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]


def island_perimeter(grid):
    """finding the perimeter of an ares soroounded by water"""
    perimeter = 0
    rowSize = len(grids)
    colSize = len(grids[0])

    for rows in range(rowSize):
        for cols in range(colSize):
            if grids[rows][cols] == 1:
                if cols - 1 < 0 or grids[rows][cols - 1] == 0:
                    perimeter += 1
                if cols + 1 == colSize or grids[rows][cols + 1] == 0:
                    perimeter += 1
                if rows - 1 < 0 or grids[rows - 1][cols] == 0:
                    perimeter += 1
                if rows + 1 == rowSize or grids[rows + 1][cols] == 0:
                    perimeter += 1
    return perimeter
