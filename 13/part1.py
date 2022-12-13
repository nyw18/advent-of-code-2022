f = open("input.txt", "r")
iteration = 1
sum = 0
fst = None
snd = None


def right_order(a, b):
    if type(a) is int and type(b) is int:
        if (a < b):
            return True
        elif a == b:
            return None
        else:
            return False
    elif type(a) is int and type(b) is list:
        a = [a]
    elif type(a) is list and type(b) is int:
        b = [b]
    i = 0
    for i in range(len(a)):
        if i < len(b):
            ordered = right_order(a[i], b[i])
            if ordered is not None:
                return ordered
        else:
            # left longer than right
            return False
    return True if i < len(b) else None


for line in f:
    input_line = line.strip()
    if len(input_line) == 0:
        fst = None
        snd = None
    elif fst is None:
        fst = eval(input_line)
    else:
        snd = eval(input_line)
        if right_order(fst, snd):
            print(iteration)
            sum += iteration
        iteration += 1

print(sum)
