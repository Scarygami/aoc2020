import os
import re
from collections import defaultdict

currentdir = os.path.dirname(os.path.abspath(__file__))


deltas = {
    "e": (1,0),
    "se": (0, 1),
    "sw": (-1, 1),
    "w": (-1, 0),
    "nw": (0, -1),
    "ne": (1, -1)
}


def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    s = re.compile("(e|se|sw|w|nw|ne)")

    directions = [s.findall(line) for line in lines]

    return directions


def prepare_lobby(filename):
    directions = parse_input(filename)

    lobby = defaultdict(bool)

    for direction in directions:
        position = (0, 0)
        for move in direction:
            position = tuple(map(sum, zip(position, deltas[move])))
        lobby[position] = not lobby[position]

    return lobby


def count_neighbours(lobby, position):
    neighbours = [tuple(map(sum, zip(position, delta))) for delta in deltas.values()]
    return sum(lobby[position] for position in neighbours)

def part1(filename):
    lobby = prepare_lobby(filename)

    return sum(lobby.values())

def part2(filename):
    lobby = prepare_lobby(filename)

    for _ in range(100):
        new_lobby = defaultdict(bool)
        blacks = [position for position, value in lobby.items() if value]
        candidates = []
        for candidate in blacks:
            candidates.append(candidate)
            candidates.extend([tuple(map(sum, zip(candidate, delta))) for delta in deltas.values()])

        candidates = set(candidates)

        for candidate in candidates:
            neighbours = count_neighbours(lobby, candidate)
            if lobby[candidate] and (neighbours == 1 or neighbours == 2):
                new_lobby[candidate] = True
            elif not lobby[candidate] and neighbours == 2:
                new_lobby[candidate] = True

        lobby = new_lobby

    return sum(lobby.values())


assert part1(os.path.join(currentdir, "testinput1.txt")) == 10

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))

assert part2(os.path.join(currentdir, "testinput1.txt")) == 2208

print("Part 2: ", part2(os.path.join(currentdir, "input.txt")))
