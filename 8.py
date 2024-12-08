from collections import defaultdict
from aoc import read_input

lines = read_input()
grid = [[c for c in line] for line in lines]

adj = defaultdict(list)
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c in [".", "#"]:
            continue
        adj[c].append((x, y))

p1 = set()
p2 = set()
for _, ps in adj.items():
    for i in range(len(ps)):
        for j in range(i + 1, len(ps)):
            x1, y1 = min([ps[i], ps[j]], key=lambda p: p[0])
            x2, y2 = max([ps[i], ps[j]], key=lambda p: p[0])

            slope = (y2 - y1) / (x2 - x1)
            sign = 1 if slope > 0 else -1
            ydiff = abs(y2 - y1)
            xdiff = abs(x2 - x1)

            steps = 0
            while x1 >= 0 and x1 < len(grid[0]) and y1 >= 0 and y1 < len(grid):
                if steps == 1:
                    p1.add((x1, y1))
                p2.add((x1, y1))
                x1 -= xdiff
                y1 += -sign * ydiff
                steps += 1

            steps = 0
            while x2 >= 0 and x2 < len(grid[0]) and y2 >= 0 and y2 < len(grid):
                if steps == 1:
                    p1.add((x2, y2))
                p2.add((x2, y2))
                x2 += xdiff
                y2 += sign * ydiff
                steps += 1

print(len(p1))
print(len(p2))
