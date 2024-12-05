import re
import sys

grid = sys.stdin.readlines()

delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
word = "XMAS"
width, height = len(grid), len(grid[0])
sum = 0

for y in range(height):
    for x in range(width):
        for dx, dy in delta:
            valid = True
            for i, w in enumerate(word):
                ix, iy =  x + i * dx, y + i * dy

                if not (0 <= ix < width and 0 <= iy < height):
                    valid = False
                    break

                if grid[ix][iy] != w:
                    valid = False
                    break
            if valid:
                sum += 1


print(sum)
