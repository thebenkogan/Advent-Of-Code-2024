from collections import deque
from aoc import DIRS, nums, read_input

lines = read_input()


def bfs(b):
    grid = [["."] * 71 for _ in range(71)]
    for line in lines[:b]:
        x, y = nums(line)
        grid[y][x] = "#"

    q = deque([(0, 0, 0)])
    ex, ey = len(grid[0]) - 1, len(grid) - 1
    seen = {(0, 0)}
    while len(q) > 0:
        x, y, steps = q.popleft()
        if x == ex and y == ey:
            return steps

        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if (
                nx in range(71)
                and ny in range(71)
                and grid[ny][nx] == "."
                and (nx, ny) not in seen
            ):
                seen.add((nx, ny))
                q.append((nx, ny, steps + 1))

    return None


print(bfs(1024))


l = 1024
r = len(lines)
while l < r:
    m = (l + r) // 2
    steps = bfs(m)
    if steps is None:
        r = m
    else:
        l = m + 1

print(lines[l - 1])
