"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).

The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.

One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.

Determine the perimeter of the island.


Review with examples:

grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]




"""

from typing import List

def islandPerimeter(grid: List[List[int]]) -> int:

    land = set()
    land_list = []
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                land.add((i, j))
                land_list.append((i, j))


    num_sides = 4 * len(land_list)
    adj_num = 0
    for tup in land_list:
        i, j = tup
        candidates = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for cand in candidates:
            cand_i, cand_j = cand

            if 0 <= cand_i and cand_i < m and 0 <= cand_j and cand_j < n:
                if grid[cand_i][cand_j] == 1:
                    adj_num += 1

    return num_sides - adj_num



if __name__ == "__main__":


    grid = [[0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]]


    num_sides = islandPerimeter(grid)


    print("Num Sides")
    print(num_sides)

    grid = [[1]]

    num_sides = islandPerimeter(grid)

    print("Num Sides")
    print(num_sides)

    grid = [[1, 0]]

    num_sides = islandPerimeter(grid)

    print("Num Sides")
    print(num_sides)
