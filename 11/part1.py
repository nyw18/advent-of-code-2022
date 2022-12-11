import re

f = open("input.txt", "r")
monkey_start_re = re.compile("Monkey (\\d+)")
start_items_re = re.compile("Starting items: (.+)")
op_re = re.compile("Operation: new = ([^ ]+) (.) ([^ ]+)")
cur_monkey = 0
monkey_items = []
monkey_op = []
monkey_test = [5, 17, 7, 13, 19, 3, 11, 2]
monkey_next = [[1, 6], [2, 5], [4, 3], [0, 7], [7, 3], [4, 2], [1, 5], [0, 6]]
monkey_times = [0 for i in range(10)]


def do_monkey_test(monkey, item_val):
    return item_val % monkey_test[monkey] == 0


def do_monkey_op(monkey, item_val):
    operand = monkey_op[monkey][1]
    if operand == "old":
        operand = item_val
    else:
        operand = int(monkey_op[monkey][1])
    if monkey_op[monkey][0] == "+":
        return item_val + operand
    elif monkey_op[monkey][0] == "*":
        return item_val * operand


for line in f:
    input_line = line.strip()
    input_match = monkey_start_re.match(input_line)
    start_match = start_items_re.match(input_line)
    op_match = op_re.match(input_line)

    if input_match:
        cur_monkey = int(input_match.group(1))
    elif start_match:
        items = start_match.group(1).split(", ")
        monkey_items.append([])
        for i in items:
            monkey_items[cur_monkey].append(int(i))
    elif op_match:
        if op_match.group(1) != "old":
            raise RuntimeError("first operand must be old")
        monkey_op.append([op_match.group(2), op_match.group(3)])

total_rounds = 20

for i in range(total_rounds):
    for j in range(len(monkey_items)):
        if len(monkey_items[j]) == 0:
            continue
        while cur_item := monkey_items[j].pop(0):
            monkey_times[j] += 1
            new_item_value = do_monkey_op(j, cur_item) // 3
            test_res = do_monkey_test(j, new_item_value)
            if test_res:
                monkey_items[monkey_next[j][0]].append(new_item_value)
            else:
                monkey_items[monkey_next[j][1]].append(new_item_value)

            if len(monkey_items[j]) == 0:
                break

list.sort(monkey_times, reverse=True)
print(monkey_times[0] * monkey_times[1])
