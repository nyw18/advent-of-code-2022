f = open("input.txt", "r")

tree_grid = []
max_score = 0

for line in f:
    input_line = line.strip()
    tree_grid.append(input_line)

for i in range(1, len(tree_grid) - 1):
    for j in range(1, len(tree_grid[i]) - 1):
        score = 1
        tree_height = tree_grid[i][j]
        viewable = 0
        for k in range(j - 1, -1, -1):
            viewable += 1
            if tree_grid[i][k] >= tree_height:
                break
        score *= viewable
        viewable = 0
        for k in range(j + 1, len(tree_grid[i])):
            viewable += 1
            if tree_grid[i][k] >= tree_height:
                break
        score *= viewable
        viewable = 0
        for k in range(i - 1, -1, -1):
            viewable += 1
            if tree_grid[k][j] >= tree_height:
                break
        score *= viewable
        viewable = 0
        for k in range(i + 1, len(tree_grid)):
            viewable += 1
            if tree_grid[k][j] >= tree_height:
                break
        score *= viewable
        if score > max_score:
            max_score = score

print(max_score)
