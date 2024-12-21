from collections import Counter
from aoc import nums, read_input

lines = read_input()

num_pos = {
    "A": (2, 3),
    "0": (1, 3),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
}

dir_pos = {
    "A": (2, 0),
    "^": (1, 0),
    ">": (2, 1),
    "v": (1, 1),
    "<": (0, 1),
}


def type_route(route, controls, empty_pos, counter=True):
    cx, cy = controls["A"]
    seqs = []
    for c in route:
        nx, ny = controls[c]
        dx = nx - cx
        dy = ny - cy
        vert = "v" * dy + "^" * -dy
        horiz = ">" * dx + "<" * -dx
        w1 = vert + horiz + "A" if (cx, ny) != empty_pos else None
        w2 = horiz + vert + "A" if (nx, cy) != empty_pos else None
        if dx > 0 and w1:
            seqs.append(w1)
        elif w2:
            seqs.append(w2)
        elif w1:
            seqs.append(w1)
        cx, cy = nx, ny

    return Counter(seqs) if counter else "".join(seqs)


routes = [type_route(line, num_pos, (0, 3), counter=False) for line in lines]
routes = [Counter([r]) for r in routes]


def iterate_robots(routes, n):
    for _ in range(n):
        new_routes = []
        for r in routes:
            new_counts = Counter()
            for route, count in r.items():
                typed = type_route(route, dir_pos, (0, 0))
                for sr, c in typed.items():
                    new_counts[sr] += c * count
            new_routes.append(new_counts)
        routes = new_routes

    total = 0
    for line, rs in zip(lines, routes):
        n = nums(line)[0]
        l = sum(len(r) * c for r, c in rs.items())
        total += l * n

    return total


print(iterate_robots(routes, 2))
print(iterate_robots(routes, 25))
