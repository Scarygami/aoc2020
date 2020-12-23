import os
from collections import deque

currentdir = os.path.dirname(os.path.abspath(__file__))


def parse_input(filename):
    with open(filename) as f:
        line = f.read()

    cups = deque([int(c) for c in line])

    return cups


def part1(filename, rounds=100):
    cups = parse_input(filename)

    for _ in range(rounds):
        current = cups[0]
        cups.rotate(-1)
        removed = [cups.popleft(), cups.popleft(), cups.popleft()]
        insert = current - 1
        while insert not in cups:
            insert = insert - 1
            if insert <= 0:
                insert = 9
        destination = cups.index(insert)

        for i in range(3):
            cups.insert(destination + i + 1, removed[i])

    while cups[0] != 1:
        cups.rotate()

    return "".join(str(c) for c in list(cups)[1:])


class Cup:
    def __init__(self, number):
        self.number = number
        self.next = None

    def __repr__(self):
        return str(self.number)


def part2(filename):
    cup_numbers = list(parse_input(filename))

    for c in range(10, 1000001):
        cup_numbers.append(c)

    cups = [Cup(c) for c in range(len(cup_numbers) + 1)]
    cups[0] = None

    for c in range(len(cup_numbers) - 1):
        cups[cup_numbers[c]].next = cups[cup_numbers[c + 1]]

    cups[cup_numbers[-1]].next = cups[cup_numbers[0]]
    current = cups[cup_numbers[0]]

    for _ in range(10000000):
        remove = [
            current.next.number,
            current.next.next.number,
            current.next.next.next.number,
        ]
        destination = len(cup_numbers) if current.number == 1 else current.number - 1
        while destination in remove:
            destination = len(cup_numbers) if destination == 1 else destination - 1

        current.next = current.next.next.next.next
        cups[remove[-1]].next = cups[destination].next
        cups[destination].next = cups[remove[0]]

        current = current.next

    return cups[1].next.number * cups[1].next.next.number


assert part1(os.path.join(currentdir, "testinput1.txt"), 10) == "92658374"
assert part1(os.path.join(currentdir, "testinput1.txt")) == "67384529"

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))

assert part2(os.path.join(currentdir, "testinput1.txt")) == 149245887792

print("Part 2: ", part2(os.path.join(currentdir, "input.txt")))
