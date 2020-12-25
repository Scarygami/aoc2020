import os

currentdir = os.path.dirname(os.path.abspath(__file__))

module = 20201227


def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return (int(lines[0]), int(lines[1]))


def part1(filename):
    public_keys = parse_input(filename)

    key = 1
    loop_size = 0
    subject_number = 7
    while key not in public_keys:
        loop_size = loop_size + 1
        key = (key * subject_number) % module

    subject_number = public_keys[1] if key == public_keys[0] else public_keys[0]

    key = 1
    for _ in range(loop_size):
        key = (key * subject_number) % module

    return key


assert part1(os.path.join(currentdir, "testinput1.txt")) == 14897079

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))
