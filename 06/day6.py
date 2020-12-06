import os
from collections import defaultdict

currentdir = os.path.dirname(os.path.abspath(__file__))


def parse_input(filename):
    """
    Returns an array of tuples of this form:
    (
        size_of_group,
        dictionary_of_questions
    )

    The dictionary_of_questions is a dictionary, with the question letter as key
    and the amount of yes answers as value
    """

    groups = []
    with open(filename) as f:
        lines = f.read().splitlines()
        group = defaultdict(int)
        size = 0
        for line in lines:
            if line == "" and len(group) > 0:
                groups.append((size, group))
                group = defaultdict(int)
                size = 0
                continue

            for question in line:
                group[question] = group[question] + 1
            size = size + 1

        if len(group) > 0:
            groups.append((size, group))

    return groups


def part1(filename):
    groups = parse_input(filename)
    return sum(len(group[1]) for group in groups)


def part2(filename):
    groups = parse_input(filename)
    return sum(
        sum(1 for question, count in group[1].items() if count == group[0])
        for group in groups
    )


assert part1(os.path.join(currentdir, "test_input.txt")) == 11

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))

assert part2(os.path.join(currentdir, "test_input.txt")) == 6

print("Part 2: ", part2(os.path.join(currentdir, "input.txt")))
