import os
from collections import defaultdict

currentdir = os.path.dirname(os.path.abspath(__file__))


def parse_input(filename):
    code = []
    with open(filename) as f:
        lines = f.read().splitlines()
        for line in lines:
            [instruction, value] = line.split(" ")
            code.append([instruction, int(value)])

    return code


def execute(code):
    """
    Runs the code until a loop is encountered, or the end of the program is reached.

    Returns a tuple (terminated, acc, visited) where terminated is True if the program
    ended normally and False if a loop has been encountered.
    """

    ip = 0
    acc = 0
    visited = defaultdict(int)

    while visited[ip] == 0:
        visited[ip] = visited[ip] + 1

        if code[ip][0] == "acc":
            acc = acc + code[ip][1]
            ip = ip + 1
        elif code[ip][0] == "nop":
            ip = ip + 1
        elif code[ip][0] == "jmp":
            ip = ip + code[ip][1]

        if ip >= len(code):
            return (True, acc, visited)
            break

    return (False, acc, visited)


def part1(filename):
    code = parse_input(filename)
    (_, acc, _) = execute(code)
    return acc


def part2(filename):
    code = parse_input(filename)

    # Run once so we only need to check the jmps/nops that are actually visited
    (_, _, visited) = execute(code)

    for ip in visited:
        if code[ip][0] == "acc":
            continue

        code[ip][0] = "nop" if code[ip][0] == "jmp" else "jmp"
        (terminated, acc, _) = execute(code)
        if terminated is True:
            return acc
        code[ip][0] = "nop" if code[ip][0] == "jmp" else "jmp"


assert part1(os.path.join(currentdir, "testinput1.txt")) == 5

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))

assert part2(os.path.join(currentdir, "testinput1.txt")) == 8

print("Part 2: ", part2(os.path.join(currentdir, "input.txt")))
