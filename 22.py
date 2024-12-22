from collections import defaultdict, deque
from aoc import read_input

lines = read_input()

p1 = 0
totals = defaultdict(int)
for line in lines:
    n = int(line)
    window = deque()
    seen = set()
    for _ in range(2000):
        start = n % 10
        n = (n * 64) ^ n
        n = n % 16777216
        n = (n // 32) ^ n
        n = n % 16777216
        n = (n * 2048) ^ n
        n = n % 16777216
        window.append((n % 10, (n % 10) - start))
        if len(window) > 4:
            window.popleft()

        seq = tuple([w[1] for w in window])
        if seq in seen:
            continue
        seen.add(seq)
        if len(seq) == 4:
            totals[seq] += window[-1][0]

    p1 += n

print(p1)
print(max(totals.values()))
