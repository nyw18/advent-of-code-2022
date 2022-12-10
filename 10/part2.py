import re

f = open("input.txt", "r")
add_re = re.compile("addx (-?\\d+)")
cycle = 1
strength = 1
cur_row = ["." for i in range(40)]

def increment_cycle():
    global cycle
    cycle += 1
    note_sum()

def note_sum():
    global cycle, cur_row, strength
    s = strength
    c = cycle - 1
    if s - 1 <= (c % 40) <= s + 1:
        cur_row[c % 40] = "#"

    if c % 40 == 0:
        print("".join(cur_row))
        cur_row = ["." for _ in range(40)]


for line in f:
    input_line = line.strip()
    input_match = add_re.match(input_line)

    if input_line == "noop":
        increment_cycle()
    elif input_match:
        add_count = int(input_match.group(1))
        increment_cycle()
        strength += add_count
        increment_cycle()
    else:
        raise RuntimeError("Unrecognised input " + input_line)
