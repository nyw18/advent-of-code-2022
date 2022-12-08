f = open("input.txt", "r")

tree_grid = []
visible = 0

for line in f:
    input_line = line.strip()
    tree_grid.append(input_line)

for i in range(len(tree_grid)):
    for j in range(len(tree_grid[i])):
        tree_height = tree_grid[i][j]
        is_visible = True
        for k in range(0, j):
            if tree_grid[i][k] >= tree_height:
                is_visible = False
                break
        if is_visible:
            visible += 1
            continue
        is_visible = True
        for k in range(j + 1, len(tree_grid[i])):
            if tree_grid[i][k] >= tree_height:
                is_visible = False
                break
        if is_visible:
            visible += 1
            continue
        is_visible = True
        for k in range(0, i):
            if tree_grid[k][j] >= tree_height:
                is_visible = False
                break
        if is_visible:
            visible += 1
            continue
        is_visible = True
        for k in range(i + 1, len(tree_grid)):
            if tree_grid[k][j] >= tree_height:
                is_visible = False
                break
        if is_visible:
            visible += 1
            continue

print(visible)
