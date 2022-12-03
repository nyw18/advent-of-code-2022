def get_priority(item):
    code = ord(item)
    if ord('z') >= code >= ord('a'):
        return code - ord('a') + 1
    elif ord('Z') >= code >= ord('A'):
        return code - ord('A') + 27
    else:
        raise RuntimeError("unrecognised code")


f = open("input.txt", "r")
front_items = {}
back_items = {}
total = 0

for line in f:
    both_items = {}
    front_items = {}
    back_items = {}
    items = line.strip()
    front, back = items[:len(items) // 2], items[len(items) // 2:]

    for i in range(len(front)):
        front_items[front[i]] = True
    for i in range(len(back)):
        back_items[back[i]] = True

    both_items = front_items.keys() & back_items.keys()

    for both_item in both_items:
        total += get_priority(both_item)

print(total)
