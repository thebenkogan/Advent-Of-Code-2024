from collections import defaultdict
from aoc import nums, read_input

lines = read_input(split_lines=False)
stones = {n: 1 for n in nums(lines)}


def blink(stones):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            lh, rh = s[: len(s) // 2], s[len(s) // 2 :]
            new_stones[int(lh)] += count
            new_stones[int(rh)] += count
        else:
            new_stones[stone * 2024] += count
    return new_stones


p1 = stones.copy()
for i in range(25):
    p1 = blink(p1)
print(sum(p1.values()))

p2 = stones.copy()
for i in range(75):
    p2 = blink(p2)
print(sum(p2.values()))
