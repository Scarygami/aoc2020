import os
import math

currentdir = os.path.dirname(os.path.abspath(__file__))

dirs = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}


def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        directions = [(line[0], int(line[1:])) for line in lines]
        return directions


def part1(filename):
    directions = parse_input(filename)

    turns = {
        ("L", 90): {
            dirs["E"]: dirs["N"],
            dirs["N"]: dirs["W"],
            dirs["W"]: dirs["S"],
            dirs["S"]: dirs["E"],
        },
        ("L", 180): {
            dirs["E"]: dirs["W"],
            dirs["N"]: dirs["S"],
            dirs["W"]: dirs["E"],
            dirs["S"]: dirs["N"],
        },
        ("L", 270): {
            dirs["E"]: dirs["S"],
            dirs["N"]: dirs["E"],
            dirs["W"]: dirs["N"],
            dirs["S"]: dirs["W"],
        },
        ("R", 90): {
            dirs["E"]: dirs["S"],
            dirs["N"]: dirs["E"],
            dirs["W"]: dirs["N"],
            dirs["S"]: dirs["W"],
        },
        ("R", 180): {
            dirs["E"]: dirs["W"],
            dirs["N"]: dirs["S"],
            dirs["W"]: dirs["E"],
            dirs["S"]: dirs["N"],
        },
        ("R", 270): {
            dirs["E"]: dirs["N"],
            dirs["N"]: dirs["W"],
            dirs["W"]: dirs["S"],
            dirs["S"]: dirs["E"],
        },
    }

    position = (0, 0)
    orientation = (1, 0)

    for instruction, amount in directions:
        if instruction in ["N", "E", "S", "W"]:
            position = (
                position[0] + amount * dirs[instruction][0],
                position[1] + amount * dirs[instruction][1],
            )
        if instruction == "F":
            position = (
                position[0] + amount * orientation[0],
                position[1] + amount * orientation[1],
            )
        if instruction in ["L", "R"]:
            orientation = turns[(instruction, amount)][orientation]

    return abs(position[0]) + abs(position[1])


def part2(filename):
    directions = parse_input(filename)
    dirs = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}

    turns = {
        ("L", 90): math.pi / 2,
        ("L", 180): math.pi,
        ("L", 270): -math.pi / 2,
        ("R", 90): -math.pi / 2,
        ("R", 180): math.pi,
        ("R", 270): math.pi / 2,
    }

    position = (0, 0)
    waypoint = (10, 1)

    for instruction, amount in directions:
        if instruction in ["N", "E", "S", "W"]:
            waypoint = (
                waypoint[0] + amount * dirs[instruction][0],
                waypoint[1] + amount * dirs[instruction][1],
            )
        if instruction == "F":
            position = (
                position[0] + amount * waypoint[0],
                position[1] + amount * waypoint[1],
            )
        if instruction in ["L", "R"]:
            angle = turns[(instruction, amount)]
            waypoint = (
                int(
                    round(waypoint[0] * math.cos(angle) - waypoint[1] * math.sin(angle))
                ),
                int(
                    round(waypoint[0] * math.sin(angle) + waypoint[1] * math.cos(angle))
                ),
            )

    return abs(position[0]) + abs(position[1])


assert part1(os.path.join(currentdir, "testinput1.txt")) == 25

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))

assert part2(os.path.join(currentdir, "testinput1.txt")) == 286

print("Part 2: ", part2(os.path.join(currentdir, "input.txt")))
