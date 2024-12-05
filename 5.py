from aoc import read_input, nums
from collections import defaultdict

lines = read_input(split_lines=False)
sections = lines.split("\n\n")

adj = defaultdict(set)
for line in sections[0].split("\n"):
    ns = nums(line)
    adj[ns[0]].add(ns[1])


p1 = 0
p2 = 0
for update in sections[1].split("\n"):
    ns = nums(update)
    s = set(ns)
    topo = defaultdict(int)
    for n in ns:
        for r in adj[n]:
            topo[r] += 1

    q = []
    for n in ns:
        if topo[n] == 0:
            q.append(n)

    order = []
    while len(q) > 0:
        a = q.pop()
        order.append(a)
        for b in adj[a]:
            topo[b] -= 1
            if topo[b] == 0 and b in s:
                q.append(b)

    if str(order) == str(ns):
        p1 += ns[len(ns) // 2]
    else:
        p2 += order[len(ns) // 2]

print(p1)
print(p2)
