import re

f = open("input.txt", "r")
tVisited = [[False for _ in range(300)] for _ in range(300)]
hPos = [150, 150]
tPos = [150, 150]


def calc_tpos():
    # Calc tail pos
    if y_diff() == 0 and abs(x_diff()) > 1:
        tPos[0] += (1 if x_diff() > 0 else -1)
    elif x_diff() == 0 and abs(y_diff()) > 1:
        tPos[1] += (1 if y_diff() > 0 else -1)
    elif abs(x_diff()) + abs(y_diff()) <= 2:
        return
    else:
        x_dir = (1 if x_diff() > 0 else -1)
        y_dir = (1 if y_diff() > 0 else -1)
        tPos[0] += x_dir
        tPos[1] += y_dir

    tVisited[tPos[0]][tPos[1]] = True


def x_diff():
    return hPos[0] - tPos[0]


def y_diff():
    return hPos[1] - tPos[1]


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
            calc_tpos()
    elif dir == 'D':
        # hPos[0] -= count
        for i in range(count):
            hPos[0] -= 1
            calc_tpos()
    elif dir == 'L':
        # hPos[1] -= count
        for i in range(count):
            hPos[1] -= 1
            calc_tpos()
    elif dir == 'R':
        # hPos[1] += count
        for i in range(count):
            hPos[1] += 1
            calc_tpos()
    else:
        raise RuntimeError("Unknown dir: " + dir)

visited_count = 0
for i in tVisited:
    for j in i:
        if j:
            visited_count += 1
print(visited_count)
