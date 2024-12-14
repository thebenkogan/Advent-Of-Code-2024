from aoc import nums, read_input

lines = read_input()
H = 103
W = 101

q1, q2, q3, q4 = 0, 0, 0, 0
for line in lines:
    ns = nums(line)
    x, y, vx, vy = ns[0], ns[1], ns[2], ns[3]

    for _ in range(100):
        x = (x + vx) % W
        y = (y + vy) % H

    if x < W // 2 and y < H // 2:
        q1 += 1
    elif x < W // 2 and y > H // 2:
        q2 += 1
    elif x > W // 2 and y < H // 2:
        q3 += 1
    elif x > W // 2 and y > H // 2:
        q4 += 1

print(q1 * q2 * q3 * q4)

# the grids have two repeating patterns
# starting at step 31 and repeating every 103 steps, there's a horizontal pattern
# starting at step 88 and repeating every 101 steps, there's a vertical pattern
# when these meet, there's a christmas tree


i = 31
step1 = 103
step2 = 101
while True:
    i += step1
    if (i - 88) % step2 == 0:
        print(i)
        break
