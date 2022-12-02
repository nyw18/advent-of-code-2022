f = open("input.txt", "r")


def move_points(move):
    match move:
        case "A" | "X":
            return 1
        case "B" | "Y":
            return 2
        case "C" | "Z":
            return 3
        case _:
            raise RuntimeError("Unknown move " + move)


def move_wins(player, oppponent):
    match oppponent:
        case "A":
            return player == "Y"
        case "B":
            return player == "Z"
        case "C":
            return player == "X"
        case _:
            raise RuntimeError("Unknown move " + player)


def game_points(player, opponent):
    if move_points(player) == move_points(opponent):
        return 3 + move_points(player)
    if move_wins(player, opponent):
        return 6 + move_points(player)
    else:
        return move_points(player)


points = 0

for line in f:
    opponent = line[0]
    player = line[2]

    points += game_points(player, opponent)

print(points)
