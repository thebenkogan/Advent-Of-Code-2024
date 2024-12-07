from aoc import nums, read_input

lines = read_input()


def eval(ns, r, t, i, ops):
    if i == len(ns):
        return r == t
    if r > t:
        return False

    for op in ops:
        nxt = r
        if op == "+":
            nxt += ns[i]
        elif op == "*":
            nxt *= ns[i]
        elif op == "||":
            nxt = int(str(nxt) + str(ns[i]))
        if eval(ns, nxt, t, i + 1, ops):
            return True

    return False


p1 = 0
p2 = 0
for line in lines:
    ns = nums(line)
    target, rest = ns[0], ns[1:]
    if eval(rest, rest[0], target, 1, ["+", "*"]):
        p1 += target
    if eval(rest, rest[0], target, 1, ["+", "*", "||"]):
        p2 += target


print(p1)
print(p2)
