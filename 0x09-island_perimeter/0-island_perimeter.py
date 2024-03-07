#!/usr/bin/python3
''' 0-island_perimeter.py: This module contains a function that returns
the perimeter of the island described in grid. '''

def island_perimeter(grid):
    ''' island_perimeter: Returns the perimeter of the island described in grid.
    Args:
        grid: A list of list of integers.
    Returns:
        The perimeter of the island described in grid.
    '''
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
