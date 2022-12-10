import re

f = open("input.txt", "r")
add_re = re.compile("addx (-?\\d+)")
cycle = 1
strength = 1
sum = 0
count_points = {20, 60, 100, 140, 180, 220}

def increment_cycle(cycles):
    global cycle, sum, count_points
    for _ in range(cycles - 1):
        cycle += 1
        note_sum()
    cycle += 1

def note_sum():
    global cycle, sum, count_points
    if cycle in count_points:
        print(strength)
        sum += strength * cycle

for line in f:
    input_line = line.strip()
    input_match = add_re.match(input_line)

    if input_line == "noop":
        increment_cycle(1)
        note_sum()
    elif input_match:
        add_count = int(input_match.group(1))
        increment_cycle(2)
        strength += add_count
        note_sum()
    else:
        raise RuntimeError("Unrecognised input " + input_line)

print(sum)
