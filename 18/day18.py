import os

currentdir = os.path.dirname(os.path.abspath(__file__))


def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines


def evaluate1(calculation):
    total = 0
    operation = "+"
    brackets = 0
    substring = ""
    for symbol in calculation:
        if symbol == " ":
            continue
        if symbol == ")":
            brackets = brackets - 1
            if brackets == 0:
                value = evaluate1(substring)
                if operation == "+":
                    total = total + value
                else:
                    total = total * value
                continue

        if brackets > 0:
            if symbol == "(":
                brackets = brackets + 1
            substring = substring + symbol
            continue

        if symbol == "(":
            brackets = 1
            substring = ""
            continue

        if symbol == "+" or symbol == "*":
            operation = symbol
            continue

        value = int(symbol)
        if operation == "+":
            total = total + value
        else:
            total = total * value

    return total


def part1(filename):
    calculations = parse_input(filename)

    return sum(evaluate1(calculation) for calculation in calculations)


def evaluate2_add(calculation):
    total = 0
    brackets = 0
    substring = ""
    for symbol in calculation:
        if symbol == " ":
            continue

        if symbol == ")":
            brackets = brackets - 1
            if brackets == 0:
                value = evaluate2_prod(substring)
                total = total + value
                continue

        if brackets > 0:
            if symbol == "(":
                brackets = brackets + 1
            substring = substring + symbol
            continue

        if symbol == "(":
            brackets = 1
            substring = ""
            continue

        if symbol == "+":
            continue

        value = int(symbol)
        total = total + value

    return total


def evaluate2_prod(calculation):
    total = 1
    brackets = 0
    substring = ""

    for symbol in calculation:
        if symbol == " ":
            continue

        if symbol == "*" and brackets == 0:
            value = evaluate2_add(substring)
            total = total * value
            substring = ""
            continue

        substring = substring + symbol

        if symbol == "(":
            brackets = brackets + 1

        if symbol == ")":
            brackets = brackets - 1

    if substring != "":
        value = evaluate2_add(substring)
        total = total * value

    return total


def part2(filename):
    calculations = parse_input(filename)

    return sum(evaluate2_prod(calculation) for calculation in calculations)


assert evaluate1("1 + 2 * 3 + 4 * 5 + 6") == 71
assert evaluate1("1 + (2 * 3) + (4 * (5 + 6))") == 51
assert evaluate1("2 * 3 + (4 * 5)") == 26
assert evaluate1("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
assert evaluate1("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
assert evaluate1("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632

assert part1(os.path.join(currentdir, "testinput1.txt")) == 122

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))

assert evaluate2_prod("1 + 2 * 3 + 4 * 5 + 6") == 231
assert evaluate2_prod("1 + (2 * 3) + (4 * (5 + 6))") == 51
assert evaluate2_prod("2 * 3 + (4 * 5)") == 46
assert evaluate2_prod("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
assert evaluate2_prod("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
assert evaluate2_prod("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340

assert part2(os.path.join(currentdir, "testinput1.txt")) == 282

print("Part 2: ", part2(os.path.join(currentdir, "input.txt")))
