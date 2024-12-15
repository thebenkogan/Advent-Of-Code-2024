from collections import deque
from aoc import read_input

lines = read_input(split_lines=False)
sections = lines.split("\n\n")
lines, moves = sections[0], sections[1]
lines = lines.split("\n")

grid = [[c for c in line] for line in lines]
C = len(grid[0])
R = len(grid)

for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == "@":
            rx, ry = x, y


def apply_move(x, y, move):
    nx, ny = x, y
    if move == ">":
        nx += 1
        dx, dy = 1, 0
    elif move == "<":
        nx -= 1
        dx, dy = -1, 0
    elif move == "v":
        ny += 1
        dx, dy = 0, 1
    elif move == "^":
        ny -= 1
        dx, dy = 0, -1
    return nx, ny, dx, dy


def get_total(grid, target):
    total = 0
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == target:
                total += 100 * y + x
    return total


for move in moves:
    if move == "\n":
        continue

    nx, ny, dx, dy = apply_move(rx, ry, move)
    if grid[ny][nx] == "#":
        continue

    if grid[ny][nx] == "O":
        bx, by = nx, ny
        while grid[by][bx] == "O":
            bx += dx
            by += dy

        if grid[by][bx] == "#":
            continue
        grid[by][bx] = "O"

    grid[ny][nx] = "@"
    grid[ry][rx] = "."
    rx, ry = nx, ny


print(get_total(grid, "O"))

g = [[c for c in line] for line in lines]
grid = []
for y, line in enumerate(g):
    row = []
    for x, c in enumerate(line):
        if c == "#":
            row.extend(["#", "#"])
        if c == "O":
            row.extend(["[", "]"])
        if c == ".":
            row.extend([".", "."])
        elif c == "@":
            row.extend(["@", "."])
    grid.append(row)
R = len(grid)
C = len(grid[0])


for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == "@":
            rx, ry = x, y

for i, move in enumerate(moves):
    if move == "\n":
        continue
    old_grid = [g.copy() for g in grid]

    nx, ny, dx, dy = apply_move(rx, ry, move)
    if grid[ny][nx] == "#":
        continue

    if grid[ny][nx] in ["[", "]"]:
        # (x, y, c) means positions (x, y) should be moved in direction (dx, dy) and replaced with c
        q = deque([(rx, ry, ".")])
        good = True
        seen = set()
        while len(q) > 0:
            sx, sy, c = q.popleft()
            if (sx, sy) in seen:
                if c != ".":
                    grid[sy][sx] = c
                continue
            seen.add((sx, sy))

            lx = sx + dx
            ly = sy + dy
            if grid[ly][lx] == "#":
                good = False
                grid = old_grid
                break

            if grid[ly][lx] in ["[", "]"]:
                q.append((lx, ly, grid[sy][sx]))
                if abs(dy) == 1 and grid[ly][lx] != grid[sy][sx]:
                    if grid[ly][lx] == "[":
                        q.append((lx + 1, ly, "."))
                    else:
                        q.append((lx - 1, ly, "."))
            else:
                grid[ly][lx] = grid[sy][sx]

            grid[sy][sx] = c

        if not good:
            continue

    grid[ny][nx] = "@"
    grid[ry][rx] = "."
    rx, ry = nx, ny

print(get_total(grid, "["))
