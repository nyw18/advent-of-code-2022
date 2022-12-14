f = open("input.txt", "r")
grid = [[0 for _ in range(200)] for _ in range(1000)]


def drop_sand(point):
    if grid[point[0]][point[1]]:
        raise RuntimeError("Space already full for sand")
    sand_pos = point
    moved = True
    while moved:
        if sand_pos[1] + 1 >= len(grid[0]):
            return False
        elif not grid[sand_pos[0]][sand_pos[1] + 1]:
            sand_pos[1] += 1
            continue
        elif not grid[sand_pos[0] - 1][sand_pos[1] + 1]:
            sand_pos[0] -= 1
            sand_pos[1] += 1
            continue
        elif not grid[sand_pos[0] + 1][sand_pos[1] + 1]:
            sand_pos[0] += 1
            sand_pos[1] += 1
            continue
        else:
            moved = False
    grid[sand_pos[0]][sand_pos[1]] = 2
    return sand_pos[1] + 1 != len(grid[0])


for line in f:
    input_line = line.strip()
    coords = input_line.split(" -> ")
    last_coord = None
    for coord in coords:
        x_coord, y_coord = coord.split(",")
        x_coord = int(x_coord)
        y_coord = int(y_coord)
        if last_coord is None:
            last_coord = [x_coord, y_coord]
        else:
            if x_coord != last_coord[0] and y_coord == last_coord[1]:
                inc = 1 if last_coord[0] < x_coord else -1
                for i in range(last_coord[0], x_coord + inc, inc):
                    grid[i][y_coord] = 1
            elif x_coord == last_coord[0] and y_coord != last_coord[1]:
                inc = 1 if last_coord[1] < y_coord else -1
                for i in range(last_coord[1], y_coord + inc, inc):
                    grid[x_coord][i] = 1
            last_coord = [x_coord, y_coord]

# Simulate sand drop at 500, 0
drop_point = [500, 0]
dropped = 0
while drop_sand(drop_point) is True:
    dropped += 1
    drop_point = [500, 0]

print(dropped)
