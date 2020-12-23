import os

currentdir = os.path.dirname(os.path.abspath(__file__))


def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    split = [i for i, line in enumerate(lines) if line == ""][0]
    player1 = [int(line) for line in lines[1:split]]
    player2 = [int(line) for line in lines[split + 2 :]]

    return (player1, player2)


def part1(filename):
    player1, player2 = parse_input(filename)

    while len(player1) > 0 and len(player2) > 0:
        p1 = player1.pop(0)
        p2 = player2.pop(0)
        if p1 > p2:
            player1.extend([p1, p2])
        else:
            player2.extend([p2, p1])

    if len(player1) > 0:
        winner = player1
    else:
        winner = player2

    return sum((i + 1) * value for i, value in enumerate(winner[::-1]))


def recursive_combat(player1, player2):
    history = []

    while len(player1) > 0 and len(player2) > 0:
        if (player1, player2) in history:
            return 1, player1

        history.append((player1.copy(), player2.copy()))

        p1 = player1.pop(0)
        p2 = player2.pop(0)

        if p1 <= len(player1) and p2 <= len(player2):
            winner, _ = recursive_combat(player1[:p1], player2[:p2])
        else:
            if p1 > p2:
                winner = 1
            else:
                winner = 2

        if winner == 1:
            player1.extend([p1, p2])
        else:
            player2.extend([p2, p1])

    if len(player1) > 0:
        return 1, player1

    return 2, player2


def part2(filename):
    player1, player2 = parse_input(filename)

    _, cards = recursive_combat(player1.copy(), player2.copy())

    return sum((i + 1) * value for i, value in enumerate(cards[::-1]))


assert part1(os.path.join(currentdir, "testinput1.txt")) == 306

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))

assert part2(os.path.join(currentdir, "testinput1.txt")) == 291

print("Part 2: ", part2(os.path.join(currentdir, "input.txt")))
