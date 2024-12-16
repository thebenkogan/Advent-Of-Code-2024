from collections import defaultdict
import heapq
import math
from aoc import DIRS, read_input

lines = read_input()
grid = [[c for c in line] for line in lines]
C = len(grid[0])
R = len(grid)

for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == "S":
            sx, sy = x, y
        if c == "E":
            ex, ey = x, y

q = [(0, sx, sy, 1, 0)]
costs = defaultdict(lambda: math.inf)
costs[(sx, sy, 1, 0)] = 0
froms = defaultdict(set)
seen = set()
while len(q) > 0:
    d, x, y, dx, dy = heapq.heappop(q)
    if (x, y, dx, dy) in seen:
        continue
    seen.add((x, y, dx, dy))

    if (x, y) == (ex, ey):
        continue

    for ddx, ddy in DIRS:
        if ddx == -dx and ddy == -dy:
            continue
        nx, ny = x + ddx, y + ddy
        is_straight = abs(ddx) == abs(dx) and abs(ddy) == abs(dy)
        cost = 1
        if not is_straight:
            cost = 1000
            nx, ny = x, y

        new_cost = d + cost
        nxt = (nx, ny, ddx, ddy)
        curr = (x, y, dx, dy)
        if grid[ny][nx] == "#" or nxt in seen:
            continue

        if new_cost > costs[nxt]:
            continue
        elif new_cost == costs[nxt]:
            froms[nxt].add(curr)
            continue

        costs[nxt] = new_cost
        froms[nxt] = {curr}
        heapq.heappush(q, (new_cost, nx, ny, ddx, ddy))

best_dir = None
best_cost = math.inf
for (x, y, dx, dy), c in costs.items():
    if c < best_cost and (x, y) == (ex, ey):
        best_cost = c
        best_dir = (dx, dy)

best_paths = {(ex, ey)}
stack = [(ex, ey, best_dir[0], best_dir[1])]
while len(stack) > 0:
    cx, cy, dx, dy = stack.pop()
    f = froms[(cx, cy, dx, dy)]
    best_paths.update([(px, py) for px, py, _, _ in f])
    stack.extend(f)


print(best_cost)
print(len(best_paths))
