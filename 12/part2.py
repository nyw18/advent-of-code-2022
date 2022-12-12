f = open("input.txt", "r")
sequence = "SabcdefghijklmnopqrstuvwxyzE"
grid = []
start = []
stack = []
shortest_len = 9999

for line in f:
    input_line = line.strip()
    grid.append(input_line)
    for i in range(len(input_line)):
        if input_line[i] == "a":
            stack.append([len(grid) - 1, i, "a", 0])


def apply_shortest(x, y, len):
    if (not shortest[x][y]) or shortest[x][y] > len:
        shortest[x][y] = len
    else:
        raise RuntimeError("should've noted shortest")


shortest = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
while next_params := stack.pop():
    x = next_params[0]
    y = next_params[1]
    cur_letter = next_params[2]
    cur_len = next_params[3]
    if shortest[x][y] is False or shortest[x][y] > cur_len:
        apply_shortest(x, y, cur_len)
        if cur_letter == sequence[-1]:
            if shortest_len > cur_len:
                shortest_len = cur_len
                shortest[x][y] = shortest_len
        else:
            prev_letter_idx = sequence.index(cur_letter) - 1
            next_letter_idx = sequence.index(cur_letter) + 1
            next_letter = sequence[0:next_letter_idx + 1]
            if cur_letter == "S":
                next_letter += "b"
            elif cur_letter == "y":
                next_letter += "E"
            if x > 0 and grid[x - 1][y] in next_letter:
                stack.append([x - 1, y, grid[x - 1][y], cur_len + 1])
            if x < len(grid) - 1 and grid[x + 1][y] in next_letter:
                stack.append([x + 1, y, grid[x + 1][y], cur_len + 1])
            if y > 0 and grid[x][y - 1] in next_letter:
                stack.append([x, y - 1, grid[x][y - 1], cur_len + 1])
            if y < len(grid[0]) - 1 and grid[x][y + 1] in next_letter:
                stack.append([x, y + 1, grid[x][y + 1], cur_len + 1])
    if len(stack) == 0:
        break
print(shortest_len)
