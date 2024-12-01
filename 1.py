from collections import Counter
from aoc import nums, read_input

lines = read_input()
left = []
right = []
for line in lines:
    ns = nums(line)
    left.append(ns[0])
    right.append(ns[1])
left = sorted(left)
right = sorted(right)

total = 0
for a, b in zip(left, right):
    total += abs(a - b)
print(total)

total = 0
cs = Counter(right)
for n in left:
    total += n * cs[n]
print(total)
