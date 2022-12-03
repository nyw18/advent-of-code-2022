def get_priority(item):
    code = ord(item)
    if ord('z') >= code >= ord('a'):
        return code - ord('a') + 1
    elif ord('Z') >= code >= ord('A'):
        return code - ord('A') + 27
    else:
        raise RuntimeError("unrecognised code")


f = open("input.txt", "r")
f_input = []
for line in f:
    f_input.append(line.strip())

front_items = {}
back_items = {}
total = 0

for i in range(len(f_input) // 3):
    both_items = {}
    front_items = {}
    mid_items = {}
    back_items = {}
    front = f_input[3 * i]
    mid = f_input[(3 * i) + 1]
    back = f_input[(3 * i) + 2]

    for j in range(len(front)):
        front_items[front[j]] = True
    for j in range(len(mid)):
        mid_items[mid[j]] = True
    for j in range(len(back)):
        back_items[back[j]] = True

    common_items = front_items.keys() & mid_items.keys() & back_items.keys()

    for common_item in common_items:
        total += get_priority(common_item)

print(total)
