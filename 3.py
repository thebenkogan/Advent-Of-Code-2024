import re
from aoc import nums, read_input

r1 = re.compile("mul\\(\\d+,\\d+\\)")
r2 = re.compile("mul\\(\\d+,\\d+\\)|do\\(\\)|don't\\(\\)")

lines = read_input(split_lines=False)
total = 0
for m in r1.findall(lines):
    ns = nums(m)
    total += ns[0] * ns[1]
print(total)

enabled = True
total = 0
for m in r2.findall(lines):
    if m == "do()":
        enabled = True
    elif m == "don't()":
        enabled = False
    elif enabled:
        ns = nums(m)
        total += ns[0] * ns[1]

print(total)
