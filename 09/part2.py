import re

f = open("input.txt", "r")
tVisited = [[False for _ in range(300)] for _ in range(300)]
hPos = [150, 150]
pos = [[150, 150] for _ in range(9)]


def calc_pos(idx):
    cmp_pos = pos[idx]
    if idx != 0:
        parent_pos = pos[idx - 1]
    else:
        parent_pos = hPos
    # Calc tail pos
    x = x_diff(parent_pos, cmp_pos)
    y = y_diff(parent_pos, cmp_pos)
    if y == 0 and abs(x) > 1:
        cmp_pos[0] += (1 if x > 0 else -1)
    elif x == 0 and abs(y) > 1:
        cmp_pos[1] += (1 if y > 0 else -1)
    elif abs(x) + abs(y) <= 2:
        # touching
        return
    else:
        x_dir = (1 if x > 0 else -1)
        y_dir = (1 if y > 0 else -1)
        cmp_pos[0] += x_dir
        cmp_pos[1] += y_dir

    pos[idx] = cmp_pos

    if idx == 8:
        tVisited[cmp_pos[0]][cmp_pos[1]] = True


def move_rope():
    for i in range(9):
        calc_pos(i)


def x_diff(a, b):
    return a[0] - b[0]


def y_diff(a, b):
    return a[1] - b[1]


tVisited[150][150] = True

for line in f:
    input_line = line.strip()
    input_re = re.compile("(.) (\\d+)")
    input_match = input_re.match(input_line)
    dir = input_line[0]
    count = int(input_match.group(2))

    if dir == 'U':
        # hPos[0] += count
        for i in range(count):
            hPos[0] += 1
            move_rope()
    elif dir == 'D':
        # hPos[0] -= count
        for i in range(count):
            hPos[0] -= 1
            move_rope()
    elif dir == 'L':
        # hPos[1] -= count
        for i in range(count):
            hPos[1] -= 1
            move_rope()
    elif dir == 'R':
        # hPos[1] += count
        for i in range(count):
            hPos[1] += 1
            move_rope()
    else:
        raise RuntimeError("Unknown dir: " + dir)

visited_count = 0
for i in tVisited:
    for j in i:
        if j:
            visited_count += 1
print(visited_count)
