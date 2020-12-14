import os
import re
import itertools

currentdir = os.path.dirname(os.path.abspath(__file__))


def create_masks(line, part=1):
    """creates OR masks to overwrite ones and AND masks to overwrite zeroes"""
    if part == 1:
        or_mask = "".join(["1" if c == "1" else "0" for c in line])
        and_mask = "".join(["0" if c == "0" else "1" for c in line])
        return ("mask", int(or_mask, 2), int(and_mask, 2))

    """For part 2 we create all possible masks from the pattern, i.e. for each
    combination we first create a mask that would work like in the first part,
    and then create the or_mask and and_mask from that pattern."""
    masks = []
    xs = [i for i in range(len(line)) if line[i] == "X"]
    basemask = ["1" if c == "1" else "X" for c in line]
    variations = itertools.product(["0", "1"], repeat=len(xs))
    for variation in variations:
        mask = basemask.copy()
        for i in range(len(xs)):
            mask[xs[i]] = variation[i]
        masks.append(create_masks("".join(mask), 1))

    return ("masks", masks)


def parse_line(line, part=1):
    if line[:4] == "mask":
        return create_masks(line[7:], part)

    matches = re.match(r"mem\[([0-9]+)\] = ([0-9]+)", line)
    return ("mem", int(matches.groups()[0]), int(matches.groups()[1]))


def parse_input(filename, part=1):
    with open(filename) as f:
        lines = f.read().splitlines()
        instructions = [parse_line(line, part) for line in lines]
        return instructions


def part1(filename):
    instructions = parse_input(filename)
    or_mask = 0
    and_mask = 0b111111111111111111111111111111111111
    mem = {}
    for instruction in instructions:
        if instruction[0] == "mask":
            or_mask = instruction[1]
            and_mask = instruction[2]
        else:
            value = instruction[2]
            value = (value | or_mask) & and_mask
            mem[instruction[1]] = value

    return sum(mem.values())


def part2(filename):
    instructions = parse_input(filename, 2)
    masks = []
    mem = {}
    for instruction in instructions:
        if instruction[0] == "masks":
            masks = instruction[1]
        else:
            for _, or_mask, and_mask in masks:
                address = (instruction[1] | or_mask) & and_mask
                mem[address] = instruction[2]

    return sum(mem.values())


assert part1(os.path.join(currentdir, "testinput1.txt")) == 165

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))

assert part2(os.path.join(currentdir, "testinput2.txt")) == 208

print("Part 2: ", part2(os.path.join(currentdir, "input.txt")))
