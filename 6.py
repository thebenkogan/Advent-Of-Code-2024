from aoc import read_input

lines = read_input()
grid = [[c for c in line] for line in lines]

dx, dy = 0, -1
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == "^":
            sx, sy = x, y

gx, gy = sx, sy
pos = set([(gx, gy)])
while gx >= 0 and gx < len(grid[0]) and gy >= 0 and gy < len(grid):
    if grid[gy][gx] == "#":
        gx -= dx
        gy -= dy
        dx, dy = -dy, dx
    else:
        pos.add((gx, gy))
    gx += dx
    gy += dy

print(len(pos))

total = 0
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c != "." or (x, y) not in pos:
            continue
        grid[y][x] = "#"

        dx, dy = 0, -1
        gx, gy = sx, sy
        seen = set()
        good = False
        while gx >= 0 and gx < len(grid[0]) and gy >= 0 and gy < len(grid):
            if ((gx, gy), (dx, dy)) in seen:
                good = True
                break
            else:
                seen.add(((gx, gy), (dx, dy)))

            if grid[gy][gx] == "#":
                gx -= dx
                gy -= dy
                dx, dy = -dy, dx
            gx += dx
            gy += dy

        if good:
            total += 1

        grid[y][x] = "."

print(total)
