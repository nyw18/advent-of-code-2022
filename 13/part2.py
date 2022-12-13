f = open("input.txt", "r")
iteration = 1
packets = []


def right_order(a, b):
    if type(a) is int and type(b) is int:
        if (a < b):
            return -1
        elif a == b:
            return 0
        else:
            return 1
    elif type(a) is int and type(b) is list:
        a = [a]
    elif type(a) is list and type(b) is int:
        b = [b]
    i = 0
    for i in range(len(a)):
        if i < len(b):
            ordered = right_order(a[i], b[i])
            if ordered != 0:
                return ordered
        else:
            # left longer than right
            return 1
    return -1 if i < len(b) else 0


for line in f:
    input_line = line.strip()
    if len(input_line) == 0:
        continue
    packets.append(eval(input_line))

packets.append([[2]])
packets.append([[6]])

from functools import cmp_to_key

packets.sort(key=cmp_to_key(right_order))

idx_a = packets.index([[2]]) + 1
idx_b = packets.index([[6]]) + 1
print(idx_a * idx_b)
