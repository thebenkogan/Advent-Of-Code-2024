from aoc import nums, read_input
import numpy as np

lines = read_input(split_lines=False)
sections = lines.split("\n\n")


def solve(ax, ay, bx, by, px, py, OFFSET=0):
    try:
        M = np.array([[ax, bx], [ay, by]])
        b = np.array([px, py]) + np.array([OFFSET, OFFSET])
        a, b = np.linalg.solve(M, b)
        ra, rb = round(a, 4), round(b, 4)
        if int(ra) == ra and int(rb) == rb:
            return 3 * ra + rb
    except:
        pass
    return 0


p1 = 0
p2 = 0
OFFSET = 10000000000000
for s in sections:
    ns = nums(s)
    ax, ay, bx, by, px, py = ns[0], ns[1], ns[2], ns[3], ns[4], ns[5]
    p1 += solve(ax, ay, bx, by, px, py)
    p2 += solve(ax, ay, bx, by, px, py, OFFSET)


print(p1)
print(p2)
