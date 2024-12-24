from aoc import read_input

lines = read_input(split_lines=False)
vals, logic = lines.split("\n\n")
vals = vals.split("\n")
logic = logic.split("\n")

vs = {}
for v in vals:
    a, b = v.split(": ")
    b = int(b)
    vs[a] = b

p1 = vs.copy()
while True:
    ok = True
    for l in logic:
        split = l.split(" ")
        a, b, op, out = split[0], split[2], split[1], split[-1]
        if a not in p1 or b not in p1:
            ok = False
            continue
        if op == "AND":
            res = p1[a] & p1[b]
        elif op == "OR":
            res = p1[a] | p1[b]
        elif op == "XOR":
            res = p1[a] ^ p1[b]
        p1[out] = res

    if ok:
        break


def get_num(l, vs):
    s = sorted([(a, k) for a, k in vs.items() if a[0] == l], reverse=True)
    b = 0
    for _, v in s:
        b = (2 * b) + v
    return b


z = get_num("z", p1)
print(z)

x, y = get_num("x", p1), get_num("y", p1)
print("x", bin(x))
print("y", bin(y))
print("a", bin(z))
print("e", bin(x + y))


for i, (expected, actual) in enumerate(reversed(list(zip(bin(x + y)[2:], bin(z)[2:])))):
    if expected == actual:
        continue
    print(i, expected, actual)

# above prints out mismatches between expected and actual bits
# I solved by hand, looking at each incorrect bit and trying to get it to match the structure of a correct bit
# I assumed z03 is a correct bit and took the gate structure of that as a reference.
# we are building an adder so all bits should have the same logic
# here are my swaps: "qrh" <> "z38", "gmh" <> "z13", "jmq" <> "z06", "cbd" <> "rqf"

# z03 reference:

# dbv XOR bcm -> z03

# dbv represents case where one of x3 or y3 is 1
# y03 XOR x03 -> dbv

# bcm represents case where z2 carry bit is on, either by x2 & y2 or carry + one z2 bit
# pbb OR mkc -> bcm
# y02 AND x02 -> pbb
# nrs AND qdt -> mkc
# x02 XOR y02 -> qdt
# dmk OR ntf -> nrs
# y01 AND x01 -> dmk
# nqp AND fht -> ntf
# x01 XOR y01 -> fht
# x00 AND y00 -> nqp
