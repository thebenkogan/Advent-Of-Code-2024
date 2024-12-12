from aoc import DIRS, read_input

lines = read_input()
grid = [[c for c in line] for line in lines]
C = len(lines[0])
R = len(lines)


def in_bounds(x, y):
    return 0 <= x < C and 0 <= y < R


seen = set()
p1 = 0
p2 = 0
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if (x, y) in seen:
            continue
        seen.add((x, y))

        stack = [(x, y)]
        perim = 0
        perims = set()
        found = set([(x, y)])
        while len(stack) > 0:
            cx, cy = stack.pop()

            for dx, dy in DIRS:
                nx, ny = cx + dx, cy + dy

                if nx < 0 or ny < 0 or nx >= C or ny >= R or grid[ny][nx] != c:
                    perims.add((nx, ny))
                    perim += 1
                    continue
                if (nx, ny) in seen:
                    continue

                stack.append((nx, ny))
                seen.add((nx, ny))
                found.add((nx, ny))

            for dx, dy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
                nx, ny = cx + dx, cy + dy
                perims.add((nx, ny))

        p1 += perim * len(found)

        sides = set()
        for cx, cy in found:
            for dx, dy in DIRS:
                nx, ny = cx + dx, cy + dy
                if in_bounds(nx, ny) and grid[ny][nx] == c:
                    continue

                # direction pointing back towards the side
                rev_dx, rev_dy = -dx, -dy

                # move down the "left" of the side
                dx1, dy1 = dy, dx
                cx1, cy1 = nx, ny
                while True:
                    cx1, cy1 = cx1 + dx1, cy1 + dy1
                    if in_bounds(cx1, cy1) and grid[cy1][cx1] == c:
                        break
                    if (
                        not in_bounds(cx1 + rev_dx, cy1 + rev_dy)
                        or grid[cy1 + rev_dy][cx1 + rev_dx] != c
                    ):
                        break

                # move down the "right" of the side
                dx2, dy2 = -dy, -dx
                cx2, cy2 = nx, ny
                while True:
                    cx2, cy2 = cx2 + dx2, cy2 + dy2
                    if in_bounds(cx2, cy2) and grid[cy2][cx2] == c:
                        break
                    if (
                        not in_bounds(cx2 + rev_dx, cy2 + rev_dy)
                        or grid[cy2 + rev_dy][cx2 + rev_dx] != c
                    ):
                        break

                # add the ends of the side and the normal direction of the side
                sides.add(((cx1, cy1), (cx2, cy2), (dx, dy)))

        p2 += len(sides) * len(found)


print(p1)
print(p2)
