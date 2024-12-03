import re
from aoc import read_input

r = re.compile("mul\\((\\d+),(\\d+)\\)")
do = re.compile("do\\(\\)")
dont = re.compile("don't\\(\\)")

lines = read_input(split_lines=False)
total = 0
for m in r.finditer(lines):
    a, b = m.groups()
    total += int(a) * int(b)
print(total)

matches = [(m.groups(), m.span()[0]) for m in r.finditer(lines)]
dos = [("do", m.span()[0]) for m in do.finditer(lines)]
donts = [("dont", m.span()[0]) for m in dont.finditer(lines)]
a = matches + dos + donts
a = sorted(a, key=lambda x: x[1])

enabled = True
total = 0
for k, _ in a:
    if k == "do":
        enabled = True
    elif k == "dont":
        enabled = False
    elif enabled:
        total += int(k[0]) * int(k[1])

print(total)
