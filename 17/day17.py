import os
from collections import defaultdict
import itertools

currentdir = os.path.dirname(os.path.abspath(__file__))


def parse_input(filename, dimensions):
    with open(filename) as f:
        lines = f.read().splitlines()

    dimension = defaultdict(int)

    for y, line in enumerate(lines):
        for x, cube in enumerate(line):
            if cube == "#":
                dimension[(x, y) + (0,) * (dimensions - 2)] = 1

    return dimension


def validate(rules, ticket):
    """return all invalid numbers in a ticket"""
    invalid = []
    for number in ticket:
        if len(rules[number]) == 0:
            invalid.append(number)

    return invalid


def get_neighbours(coordinate):
    deltas = itertools.product([-1, 0, 1], repeat=len(coordinate))
    neighbours = [tuple(a + b for a, b in zip(coordinate, delta)) for delta in deltas]
    neighbours = [neighbour for neighbour in neighbours if neighbour != coordinate]
    return neighbours


def evolve(dimension):
    new_dimension = defaultdict(int)

    candidates = []
    for coordinate in dimension.keys():
        candidates.append(coordinate)
        candidates.extend(get_neighbours(coordinate))

    candidates = set(candidates)

    for candidate in candidates:
        neighbours = get_neighbours(candidate)
        count = sum(dimension[neighbour] for neighbour in neighbours)
        if count == 3 or (dimension[candidate] == 1 and count == 2):
            new_dimension[candidate] = 1

    return new_dimension


def boot(filename, dimensions):
    dimension = parse_input(filename, dimensions)
    for _ in range(6):
        dimension = evolve(dimension)
    return sum(dimension.values())


def part1(filename):
    return boot(filename, 3)


def part2(filename):
    return boot(filename, 4)


assert part1(os.path.join(currentdir, "testinput1.txt")) == 112

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))

assert part2(os.path.join(currentdir, "testinput1.txt")) == 848

print("Part 2: ", part2(os.path.join(currentdir, "input.txt")))
