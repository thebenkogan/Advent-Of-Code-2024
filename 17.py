from aoc import nums, read_input

lines = read_input(split_lines=False)
regs, prog = lines.split("\n\n")


def get_combo(regs, operand):
    if operand < 4:
        return operand
    elif operand == 4:
        return regs["A"]
    elif operand == 5:
        return regs["B"]
    elif operand == 6:
        return regs["C"]
    else:
        raise ValueError("Invalid operand")


regs = nums(regs)
regs = {"A": regs[0], "B": regs[1], "C": regs[2]}
prog = nums(prog)
insts = []
for i in range(0, len(prog), 2):
    insts.append((prog[i], prog[i + 1]))


def run(regs, insts):
    output = []
    ip = 0
    while ip >= 0 and ip < len(insts):
        op, operand = insts[ip]
        if op == 0:
            numerator = regs["A"]
            denominator = 2 ** get_combo(regs, operand)
            regs["A"] = numerator // denominator
        elif op == 1:
            regs["B"] = operand ^ regs["B"]
        elif op == 2:
            regs["B"] = get_combo(regs, operand) % 8
        elif op == 3:
            if regs["A"] != 0:
                ip = operand
                continue
        elif op == 4:
            regs["B"] = regs["C"] ^ regs["B"]
        elif op == 5:
            output.append(get_combo(regs, operand) % 8)
        elif op == 6:
            numerator = regs["A"]
            denominator = 2 ** get_combo(regs, operand)
            regs["B"] = numerator // denominator
        elif op == 7:
            numerator = regs["A"]
            denominator = 2 ** get_combo(regs, operand)
            regs["C"] = numerator // denominator
        ip += 1

    return ",".join(map(str, output))


print(run(regs, insts))

# here is the program
# while A != 0:
# B = A % 8 -> B = top 3 bits of A
# B = B ^ 2 -> B = top 3 bits of A, with second bit flipped
# C = A // 2**B -> C = bits of A right shifted B times
# B = B ^ C -> toggle B with the shifted bits
# A = A // 8 -> right shift A 3 times
# B = B ^ 7 -> toggle all B bits
# print(B % 8) -> output the last 3 bits

# keep trying increasing A's until it prints the next digit of the program
# take the previous run's answer as the binary prefix, try more A's after that
# repeat until prefix yields the entire program


def concat_bits(a, b):
    return int(str(bin(a)[2:]) + str(bin(b)[2:]), 2) if b != 0 else a


def last_n_bits(a, n):
    b = str(bin(a)[2:])
    return int(b[-n:], 2)


best = -1
prefix = 0
# run until len(prog) - 3 is purely experimental, idk how to determine it
while best != len(prog) - 3:
    for a in range(1, 1000000000000):
        a = concat_bits(a, prefix)
        start_a = a
        b, c = regs["B"], regs["C"]
        i = 0
        found = False
        while a != 0:
            b = a % 8
            b = b ^ 2
            c = a // 2**b
            b = b ^ c
            a = a // 8
            b = b ^ 7
            out = b % 8
            if out != prog[i]:
                break
            if i > best:
                best = i
                prefix = last_n_bits(start_a, 3 * (i + 1))
                found = True
                break
            i += 1

        if found:
            break

progstr = ",".join(map(str, prog))
for a in range(1, 1000000000000):
    regs = regs.copy()
    a = concat_bits(a, prefix)
    regs["A"] = a
    b, c = regs["B"], regs["C"]
    if run(regs, insts) == progstr:
        print(a)
        break
