from aoc import read_input

lines = read_input(split_lines=False)


def checksum(space):
    total = 0
    for i, n in enumerate(space):
        if n == ".":
            continue
        total += int(n) * i
    return total


space = []
free = False
ID = 0
free_space = {}
for c in lines:
    n = int(c)
    if free:
        free_space[len(space)] = n
        for _ in range(n):
            space.append(".")
    else:
        for _ in range(n):
            space.append(str(ID))
        ID += 1
    free = not free

space1 = list(space)
for i, c in enumerate(space1):
    if c == ".":
        l = i
        break

r = len(space1) - 1
while l < r:
    if space1[l] != ".":
        l += 1
        continue
    if space1[r] == ".":
        r -= 1
        continue
    space1[l] = space1[r]
    space1[r] = "."
    l += 1
    r -= 1

print(checksum(space1))

space2 = list(space)
r = len(space2) - 1
seen = set()
while r > 0:
    if space2[r] == ".":
        r -= 1
        continue
    c = space2[r]
    if c in seen:
        r -= 1
        continue
    seen.add(c)

    file_size = 0
    while space2[r] == c and r >= 0:
        file_size += 1
        r -= 1

    candidates = [(k, v) for (k, v) in free_space.items() if k <= r and v >= file_size]
    if len(candidates) == 0:
        continue

    i, length = min(candidates, key=lambda x: x[0])
    for j in range(i, i + file_size):
        space2[j] = c
    for j in range(r + 1, r + 1 + file_size):
        space2[j] = "."
    del free_space[i]

    if file_size < length:
        free_space[i + file_size] = length - file_size


print(checksum(space2))
