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
    rowSize = len(grid)
    colSize = len(grid[0])

    for rows in range(rowSize):
        for cols in range(colSize):
            if grid[rows][cols] == 1:
                if cols - 1 < 0 or grid[rows][cols - 1] == 0:
                    perimeter += 1
                if cols + 1 == colSize or grid[rows][cols + 1] == 0:
                    perimeter += 1
                if rows - 1 < 0 or grid[rows - 1][cols] == 0:
                    perimeter += 1
                if rows + 1 == rowSize or grid[rows + 1][cols] == 0:
                    perimeter += 1
    return perimeter
