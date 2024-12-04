from aoc import DIAG_DIRS, read_input

lines = read_input()
grid = [[c for c in line] for line in lines]

total = 0
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c != "X":
            continue
        for dx, dy in DIAG_DIRS:
            xx, yy = x + dx, y + dy
            s = ""
            while (
                xx >= 0
                and xx < len(grid[0])
                and yy >= 0
                and yy < len(grid)
                and len(s) < 3
            ):
                s += grid[yy][xx]
                xx += dx
                yy += dy
            if s == "MAS":
                total += 1

print(total)

total = 0
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c != "A" or x == 0 or y == 0 or y == len(grid) - 1 or x == len(grid[0]) - 1:
            continue

        tr, br, tl, bl = (
            grid[y - 1][x + 1],
            grid[y + 1][x + 1],
            grid[y - 1][x - 1],
            grid[y + 1][x - 1],
        )
        if (tr + bl) in ("MS", "SM") and (tl + br) in ("MS", "SM"):
            total += 1

print(total)
