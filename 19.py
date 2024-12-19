from aoc import read_input

lines = read_input(split_lines=False)

towels, patterns = lines.split("\n\n")
towels = towels.split(", ")
patterns = patterns.split("\n")


cache = {}


def count_ways(towels, pattern, running):
    key = (pattern, running)
    if key in cache:
        return cache[key]

    if len(running) >= len(pattern):
        return 1 if running == pattern else 0

    total = 0
    for t in towels:
        if pattern[len(running) : len(running) + len(t)] != t:
            continue
        total += count_ways(towels, pattern, running + t)

    cache[key] = total
    return total


p1 = 0
p2 = 0
for p in patterns:
    cnt = count_ways(towels, p, "")
    if cnt > 0:
        p1 += 1
    p2 += cnt

print(p1)
print(p2)
