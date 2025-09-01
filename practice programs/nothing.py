import math
import os
import random
import re
import sys


def numCells(grid):
    m, n = len(grid), len(grid[0])
    dominant_count = 0

    # directions: 8 neighbors (up, down, left, right, diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for i in range(m):
        for j in range(n):
            val = grid[i][j]
            neighbors = []

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n:
                    neighbors.append(grid[ni][nj])

            if all(val > nb for nb in neighbors):
                dominant_count += 1

    return dominant_count


if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []
    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)
    fptr.write(str(result) + '\n')
    fptr.close()