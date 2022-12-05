import re


def parse_stack_row(input_row):
    idx = 1
    while idx < len(input_row):
        item = input_row[idx]
        if item != ' ':
            stacks[(idx - 1)//4].append(item)
        idx += 4


f = open("input.txt", "r")
stack_count = 9
stacks = [[] for _ in range(stack_count)]
phase = 0

for line in f:
    input_row = line.rstrip()
    if not len(input_row):
        phase += 1
        continue

    if phase == 0 and input_row[1] != '1':
        parse_stack_row(input_row)
    elif input_row[0] == 'm':
        command_re = re.compile("move (\\d+) from (\\d) to (\\d)")
        command_match = command_re.match(input_row)
        count = int(command_match.group(1))
        stack_from = int(command_match.group(2))
        stack_to = int(command_match.group(3))

        for i in range(count):
            if len(stacks[stack_from - 1]):
                item = stacks[stack_from - 1].pop(0)
                stacks[stack_to - 1].insert(0, item)
            else:
                print("Skip: " + input_row + ":" + str(i))

print([stack[0] if len(stacks) else '.' for stack in stacks])
