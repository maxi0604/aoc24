import sys

grid = sys.stdin.readlines()

delta = [(0, 0), (2, 0), (1, 1), (0, 2), (2, 2)]
words = ["MSAMS", "SSAMM", "SMASM", "MMASS"]
width, height = len(grid[0]), len(grid)
sum = 0

for y in range(height):
    for x in range(width):
            for word in words:
                valid = True
                for i, (dx, dy) in enumerate(delta):
                    ix, iy =  x + dx, y + dy

                    if not (0 <= ix < width and 0 <= iy < height):
                        valid = False
                        break

                    if grid[iy][ix] != word[i]:
                        valid = False
                        break

                if valid:
                    sum += 1


print(sum)
