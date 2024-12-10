from aoc import DIRS, read_input

lines = read_input()
grid = [[int(c) for c in line] for line in lines]

starts = []
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == 0:
            starts.append((x, y))


def dfs(grid, sx, sy):
    stack = [(sx, sy)]
    seen = set([(sx, sy)])
    total = 0
    while len(stack) > 0:
        x, y = stack.pop()
        if grid[y][x] == 9:
            total += 1

        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if (
                nx < 0
                or ny < 0
                or nx >= len(grid[0])
                or ny >= len(grid)
                or (nx, ny) in seen
                or grid[ny][nx] - grid[y][x] != 1
            ):
                continue

            seen.add((nx, ny))
            stack.append((nx, ny))

    return total


def dfs_unique_paths(grid, sx, sy):
    stack = [(sx, sy, set([(sx, sy)]))]
    total = 0
    while len(stack) > 0:
        x, y, seen = stack.pop()
        if grid[y][x] == 9:
            total += 1

        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if (
                nx < 0
                or ny < 0
                or nx >= len(grid[0])
                or ny >= len(grid)
                or (nx, ny) in seen
                or grid[ny][nx] - grid[y][x] != 1
            ):
                continue

            new_seen = seen.copy()
            new_seen.add((nx, ny))
            stack.append((nx, ny, new_seen))

    return total


p1 = sum(dfs(grid, *start) for start in starts)
p2 = sum(dfs_unique_paths(grid, *start) for start in starts)
print(p1)
print(p2)
