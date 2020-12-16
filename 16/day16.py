import os
from collections import defaultdict
from itertools import chain
import re

currentdir = os.path.dirname(os.path.abspath(__file__))


def create_rules(lines):
    rules = defaultdict(set)
    attributes = set([])
    for line in lines:
        match = re.match(r"([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)", line)
        groups = match.groups()
        attribute = groups[0]
        attributes.add(attribute)
        a, b, c, d = [int(x) for x in groups[1:]]

        for x in chain(range(a, b + 1), range(c, d + 1)):
            rules[x].add(attribute)

    return rules, attributes


def create_ticket(line):
    return [int(i) for i in line.split(",")]


def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    splits = [i for i, line in enumerate(lines) if line == ""]
    rule_block = lines[: splits[0]]
    my_ticket_block = lines[splits[0] + 2]
    other_tickets_block = lines[splits[1] + 2 :]

    rules, attributes = create_rules(rule_block)
    my_ticket = create_ticket(my_ticket_block)
    other_tickets = [create_ticket(line) for line in other_tickets_block]

    return rules, attributes, my_ticket, other_tickets


def validate(rules, ticket):
    """return all invalid numbers in a ticket"""
    invalid = []
    for number in ticket:
        if len(rules[number]) == 0:
            invalid.append(number)

    return invalid


def part1(filename):
    rules, _, _, other_tickets = parse_input(filename)
    invalid = []
    for ticket in other_tickets:
        invalid.extend(validate(rules, ticket))

    return sum(invalid)


def part2(filename, prefix="departure"):
    rules, attributes, my_ticket, other_tickets = parse_input(filename)

    tickets = [ticket for ticket in other_tickets if len(validate(rules, ticket)) == 0]

    positions = []
    for position in range(len(tickets[0])):
        valid_attributes = attributes.copy()
        for ticket in tickets:
            valid_attributes = valid_attributes & rules[ticket[position]]

        positions.append(valid_attributes)

    while len([position for position in positions if len(position) > 1]) > 0:
        for position in positions:
            if len(position) == 1:
                for position2 in positions:
                    if len(position2) > 1:
                        position2.difference_update(position)

    final_positions = {}
    for p, position in enumerate(positions):
        final_positions[list(position)[0]] = p

    result = 1
    for attribute, position in final_positions.items():
        if attribute.startswith(prefix):
            result = result * my_ticket[position]

    return result


assert part1(os.path.join(currentdir, "testinput1.txt")) == 71

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))

assert part2(os.path.join(currentdir, "testinput2.txt"), "") == 1716

print("Part 2: ", part2(os.path.join(currentdir, "input.txt")))
