import os

currentdir = os.path.dirname(os.path.abspath(__file__))


def parse_input(filename):
    with open(filename) as f:
        line = f.read()
        numbers = [int(number) for number in line.split(",")]
        return numbers


def last_turn(numbers, turns=2020):
    spoken = {}
    for index, number in enumerate(numbers[:-1]):
        spoken[number] = index
    last_spoken = numbers[-1]
    for turn in range(len(numbers), turns):
        if last_spoken in spoken:
            age = turn - spoken[last_spoken] - 1
        else:
            age = 0
        spoken[last_spoken] = turn - 1
        last_spoken = age

    return last_spoken


def part1(filename):
    numbers = parse_input(filename)
    return last_turn(numbers, 2020)


def part2(filename):
    numbers = parse_input(filename)
    return last_turn(numbers, 30000000)


assert part1(os.path.join(currentdir, "testinput1.txt")) == 436

assert last_turn([1, 3, 2], 2020) == 1
assert last_turn([2, 1, 3], 2020) == 10
assert last_turn([1, 2, 3], 2020) == 27
assert last_turn([2, 3, 1], 2020) == 78
assert last_turn([3, 2, 1], 2020) == 438
assert last_turn([3, 1, 2], 2020) == 1836

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))

assert part2(os.path.join(currentdir, "testinput1.txt")) == 175594

assert last_turn([1, 3, 2], 30000000) == 2578
assert last_turn([2, 1, 3], 30000000) == 3544142
assert last_turn([1, 2, 3], 30000000) == 261214
assert last_turn([2, 3, 1], 30000000) == 6895259
assert last_turn([3, 2, 1], 30000000) == 18
assert last_turn([3, 1, 2], 30000000) == 362

print("Part 2: ", part2(os.path.join(currentdir, "input.txt")))
