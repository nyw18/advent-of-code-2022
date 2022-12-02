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


def move_wins_points(result, oppponent):
    win = result == "Z"
    match oppponent:
        case "A":
            return move_points("Y") if win else move_points("Z")
        case "B":
            return move_points("Z") if win else move_points("X")
        case "C":
            return move_points("X") if win else move_points("Y")
        case _:
            raise RuntimeError("Unknown move result " + result)


def game_points(result, opponent):
    match result:
        case "Y":
            return 3 + move_points(opponent)
        case "X" | "Z":
            move_score = move_wins_points(result, opponent)
            if result == "Z":
                move_score += 6
            return move_score
        case _:
            raise RuntimeError("Unknown result " + result)


points = 0

for line in f:
    opponent = line[0]
    result = line[2]

    points += game_points(result, opponent)

print(points)
