import os
from copy import deepcopy
from collections import defaultdict
from math import sqrt
import itertools

currentdir = os.path.dirname(os.path.abspath(__file__))

TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3


class Tile:
    def __init__(self, id, lines):
        self.id = id
        self.data = [[x for x in line] for line in lines]
        self.create_orientations()

    def create_orientations(self):
        self.orientations = []
        current = deepcopy(self.data)
        for _ in range(4):
            current = list(zip(*reversed(current)))
            self.orientations.append(deepcopy(current))
            self.orientations.append(deepcopy(current[::-1]))

    def match_border(self, orientation, side):
        data = self.orientations[orientation]
        if side == 0:
            return list(data[0])
        if side == 2:
            return list(data[-1])
        if side == 1:
            return [line[-1] for line in data]
        if side == 3:
            return [line[0] for line in data]

    def inside(self, orientation):
        data = self.orientations[orientation]
        return [list(line[1:-1]) for line in data[1:-1]]


def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    tiles = []
    i = 0
    while i < len(lines):
        id = int(lines[i][5:9])
        tiles.append(Tile(id, lines[i + 1 : i + 11]))
        i = i + 12

    return tiles


def part1(filename):
    tiles = parse_input(filename)

    partners = defaultdict(set)

    for a in range(len(tiles) - 1):
        for o_a in range(8):
            for side in range(4):
                border_a = tiles[a].match_border(o_a, side)
                for b in range(a + 1, len(tiles)):
                    for o_b in range(8):
                        border_b = tiles[b].match_border(o_b, (side + 2) % 4)
                        if border_a == border_b:
                            partners[(a, tiles[a].id)].add((b, tiles[b].id))
                            partners[(b, tiles[b].id)].add((a, tiles[a].id))

    value = 1
    for key, values in partners.items():
        if len(values) == 2:
            value = value * key[1]

    return value


def part2(filename):
    tiles = parse_input(filename)

    matches = {}
    partners = defaultdict(set)

    for a in range(len(tiles) - 1):
        for o_a in range(8):
            for side in range(4):
                border_a = tiles[a].match_border(o_a, side)
                for b in range(a + 1, len(tiles)):
                    for o_b in range(8):
                        border_b = tiles[b].match_border(o_b, (side + 2) % 4)
                        if border_a == border_b:
                            matches[(a, o_a, side)] = (b, o_b)
                            matches[(b, o_b, (side + 2) % 4)] = (a, o_a)
                            partners[a].add(b)
                            partners[b].add(a)

    puzzle_size = int(sqrt(len(tiles)))
    puzzle = [[None for _ in range(puzzle_size)] for _ in range(puzzle_size)]

    corners = [id for id, values in partners.items() if len(values) == 2]

    corner = corners[0]
    # Find the orientation to place the corner in the top left corner
    for orientation in range(8):
        if (corner, orientation, RIGHT) in matches and (
            corner,
            orientation,
            BOTTOM,
        ) in matches:
            puzzle[0][0] = (corner, orientation)
            break

    for x in range(puzzle_size - 1):
        for y in range(puzzle_size):
            if y < puzzle_size - 1:
                puzzle[x][y + 1] = matches[puzzle[x][y] + (RIGHT,)]
            puzzle[x + 1][y] = matches[puzzle[x][y] + (BOTTOM,)]

    full_puzzle = [
        [tiles[puzzle[x][y][0]].inside(puzzle[x][y][1]) for y in range(puzzle_size)]
        for x in range(puzzle_size)
    ]

    image = []
    for x in range(puzzle_size):
        for x1 in range(8):
            line = []
            for y in range(puzzle_size):
                line.extend(full_puzzle[x][y][x1])
            image.append(line)

    orientations = []
    current = deepcopy(image)
    for _ in range(4):
        current = [list(line) for line in zip(*reversed(current))]
        orientations.append(deepcopy(current))
        orientations.append(deepcopy(current[::-1]))

    monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
    monster_h = len(monster)
    monster_w = len(monster[0])
    image_h = len(image)
    image_w = len(image[0])

    for image in orientations:
        monsters = 0
        for x in range(image_h - monster_h):
            for y in range(image_w - monster_w):
                monster_found = True
                for (x1, y1) in itertools.product(range(monster_h), range(monster_w)):
                    if monster[x1][y1] == "#" and image[x + x1][y + y1] != "#":
                        monster_found = False
                        break

                if monster_found:
                    monsters = monsters + 1
                    for (x1, y1) in itertools.product(
                        range(monster_h), range(monster_w)
                    ):
                        if monster[x1][y1] == "#":
                            image[x + x1][y + y1] = "O"

        if monsters > 0:
            return sum(line.count("#") for line in image)

    return 0


assert part1(os.path.join(currentdir, "testinput1.txt")) == 20899048083289

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))

assert part2(os.path.join(currentdir, "testinput1.txt")) == 273

print("Part 2: ", part2(os.path.join(currentdir, "input.txt")))
