import os

currentdir = os.path.dirname(os.path.abspath(__file__))


def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        numbers = [int(line) for line in lines if line != ""]

    return numbers


def is_valid(number, numbers):
    for a in numbers:
        b = number - a
        if a != b and b in numbers:
            return True

    return False


def part1(filename, preamble=25):
    numbers = parse_input(filename)
    for i in range(preamble, len(numbers)):
        if not is_valid(numbers[i], numbers[i - preamble : i]):
            return numbers[i]

    return None


def part2(filename, preamble=25):
    numbers = parse_input(filename)
    goal = part1(filename, preamble)
    for i in range(len(numbers)):
        total = 0
        for j in range(i, len(numbers)):
            total = total + numbers[j]
            if total == goal:
                return min(numbers[i : j + 1]) + max(numbers[i : j + 1])
            if total > goal:
                break


assert part1(os.path.join(currentdir, "testinput1.txt")) is None
assert part1(os.path.join(currentdir, "testinput2.txt")) is None
assert part1(os.path.join(currentdir, "testinput3.txt")) == 100
assert part1(os.path.join(currentdir, "testinput4.txt")) == 50
assert part1(os.path.join(currentdir, "testinput5.txt")) is None
assert part1(os.path.join(currentdir, "testinput6.txt")) == 65
assert part1(os.path.join(currentdir, "testinput7.txt")) is None
assert part1(os.path.join(currentdir, "testinput8.txt")) is None
assert part1(os.path.join(currentdir, "testinput9.txt"), 5) == 127

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))

assert part2(os.path.join(currentdir, "testinput9.txt"), 5) == 62

print("Part 2: ", part2(os.path.join(currentdir, "input.txt")))
