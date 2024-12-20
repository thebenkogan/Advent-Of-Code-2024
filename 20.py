from collections import deque
from aoc import DIRS, read_input

lines = read_input()
grid = [[c for c in line] for line in lines]
R = len(grid)
C = len(grid[0])

for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == "E":
            ex, ey = x, y

q = deque([(ex, ey, 0)])
dist = {}
seen = {(ex, ey)}
while len(q) > 0:
    x, y, steps = q.popleft()
    dist[(x, y)] = steps

    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if (nx, ny) in seen or grid[ny][nx] == "#":
            continue
        seen.add((nx, ny))
        q.append((nx, ny, steps + 1))


# for each position, BFS to all positions max_steps away, check the difference in end distance
def check_cheats(max_steps):
    total = 0
    for sy, line in enumerate(grid):
        for sx, c in enumerate(line):
            if c == "E" or c == "#":
                continue

            d1 = dist[(sx, sy)]
            q = deque([(sx, sy, 0)])
            seen = {(sx, sy)}
            while len(q) > 0:
                x, y, steps = q.popleft()
                if steps > max_steps:
                    continue
                if grid[y][x] != "#":
                    d2 = dist[(x, y)]
                    if (d1 - d2) - steps >= 100:
                        total += 1

                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= C or ny < 0 or ny >= R or (nx, ny) in seen:
                        continue
                    seen.add((nx, ny))
                    q.append((nx, ny, steps + 1))

    return total


print(check_cheats(2))
print(check_cheats(20))
