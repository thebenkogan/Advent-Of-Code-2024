from collections import defaultdict
from itertools import combinations
from aoc import read_input

lines = read_input()

adj = defaultdict(list)
for line in lines:
    a, b = line.split("-")
    adj[a].append(b)
    adj[b].append(a)

connected = set()
for k, v in adj.items():
    opts = set(v + [k])
    sets = {k: opts}
    for n in v:
        sets[n] = set([a for a in adj[n] if a in opts] + [n])

    for candidate in sets.values():
        if len(candidate) < 3:
            continue
        i = candidate
        for n in candidate:
            i = i.intersection(sets[n])
        if len(i) != len(candidate):
            continue
        connected.add(tuple(sorted(i)))

threes = set()
for c in connected:
    if len(c) < 3:
        continue
    for a, b, c in combinations(c, 3):
        if "t" in a[0] + b[0] + c[0]:
            threes.add((a, b, c))
print(len(threes))

biggest = max(connected, key=len)
print(",".join(sorted(biggest)))
