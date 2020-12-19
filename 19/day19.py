import os
import itertools
import re

currentdir = os.path.dirname(os.path.abspath(__file__))


def create_rules(lines):
    rules = {}

    for line in lines:
        number_string, rule_string = line.split(": ")
        number = int(number_string)
        if rule_string == '"a"' or rule_string == '"b"':
            rules[number] = [rule_string[1]]
            continue

        ors = rule_string.split(" | ")
        rule = []
        for sub_rule_string in ors:
            sub_rule = [int(value) for value in sub_rule_string.split(" ")]
            rule.append(sub_rule)

        rules[number] = rule

    return rules


def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    split = [i for i, line in enumerate(lines) if line == ""][0]

    rule_block = lines[:split]
    messages = lines[split + 1 :]
    rules = create_rules(rule_block)

    return (rules, messages)


def unravel(rule, rules):
    if rule == ["a"] or rule == ["b"]:
        return rule

    new_rule = []
    for sub_rule in rule:
        unraveled_sub_rule = [unravel(rules[part], rules) for part in sub_rule]
        new_sub_rules = list(itertools.product(*unraveled_sub_rule))
        new_rule.extend(["".join(new_sub_rule) for new_sub_rule in new_sub_rules])

    return new_rule


def is_valid(message, rules):
    return message in rules


def part1(filename):
    rules, messages = parse_input(filename)
    zero_rule = unravel(rules[0], rules)

    valid = [message for message in messages if is_valid(message, zero_rule)]

    return len(valid)


def chunkstring(string, length):
    return (string[0 + i : length + i] for i in range(0, len(string), length))


def is_valid2(message, rule_42, rule_31):
    part_len = len(rule_42[0])
    if len(message) % part_len != 0:
        return False

    parts = chunkstring(message, part_len)
    valid_rules = "".join(
        [
            "x" if part in rule_42 else ("y" if part in rule_31 else " ")
            for part in parts
        ]
    )

    # Message always consist of 42's followed by 31's
    if re.match("^x+y+$", valid_rules) is None:
        return False

    # Minimum message is (42, 42, 31)
    # There's at least one 42 more than 31's in each message
    if valid_rules.count("x") < valid_rules.count("y") + 1:
        return False

    return True


def part2(filename):
    rules, messages = parse_input(filename)

    rule_42 = unravel(rules[42], rules)
    rule_31 = unravel(rules[31], rules)

    valid = [message for message in messages if is_valid2(message, rule_42, rule_31)]

    return len(valid)


assert part1(os.path.join(currentdir, "testinput1.txt")) == 2
assert part1(os.path.join(currentdir, "testinput2.txt")) == 2

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))

assert part2(os.path.join(currentdir, "testinput3.txt")) == 12

print("Part 2: ", part2(os.path.join(currentdir, "input.txt")))
