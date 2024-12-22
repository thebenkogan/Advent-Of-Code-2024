from aoc import read_input

lines = read_input()

total = 0
all_seqs = set()
rs = []
rs_seqs = []
for line in lines:
    n = int(line)
    results = []
    for _ in range(2000):
        start = n % 10
        n = (n * 64) ^ n
        n = n % 16777216

        n = (n // 32) ^ n
        n = n % 16777216

        n = (n * 2048) ^ n
        n = n % 16777216
        results.append((n, (n % 10) - start))

    total += n

    seqs = {}
    for i in range(0, len(results) - 3):
        seq = tuple([results[i + j][1] for j in range(4)])
        if seq not in seqs:
            seqs[seq] = results[i + 3][0] % 10

    all_seqs.update(seqs.keys())
    rs.append(results)
    rs_seqs.append(seqs)

print(total)

best = 0
for seq in all_seqs:
    total = 0
    for r, rs_seq in zip(rs, rs_seqs):
        if seq not in rs_seq:
            continue
        total += rs_seq[seq]
    best = max(best, total)

print(best)
