from aoc import nums, read_input

lines = read_input()


def is_safe(ns, retry):
    dec = ns[0] > ns[1]
    good = True
    for i in range(len(ns) - 1):
        curr, nxt = ns[i], ns[i + 1]
        diff = abs(curr - nxt)
        if dec and curr < nxt or not dec and curr > nxt or diff < 1 or diff > 3:
            good = False
    if good:
        return True

    if retry:
        for i in range(len(ns)):
            new_ns = ns[:i] + ns[i + 1 :]
            if is_safe(new_ns, False):
                return True

    return False


p1 = 0
p2 = 0
for line in lines:
    ns = nums(line)
    p1 += is_safe(ns, False)
    p2 += is_safe(ns, True)

print(p1)
print(p2)
