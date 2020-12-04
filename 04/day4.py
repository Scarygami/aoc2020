import os

currentdir = os.path.dirname(os.path.abspath(__file__))


def parse_input(filename):
    passports = []
    with open(filename) as f:
        lines = f.read().splitlines()
        passport = {}
        for line in lines:
            if line == "" and len(passport) > 0:
                passports.append(passport)
                passport = {}
                continue

            parts = [part.split(":") for part in line.split(" ")]
            for part in parts:
                passport[part[0]] = part[1]

        if len(passport) > 0:
            passports.append(passport)

    return passports


def is_valid_part1(passport):
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for part in required:
        if part not in passport:
            return False

    return True


def is_valid_part2(passport):
    if not is_valid_part1(passport):
        return False

    if not passport["byr"].isnumeric():
        return False
    byr = int(passport["byr"])
    if byr < 1920 or byr > 2002:
        return False

    if not passport["iyr"].isnumeric():
        return False
    iyr = int(passport["iyr"])
    if iyr < 2010 or iyr > 2020:
        return False

    if not passport["eyr"].isnumeric():
        return False
    eyr = int(passport["eyr"])
    if eyr < 2020 or eyr > 2030:
        return False

    h_unit = passport["hgt"][-2:]
    h = passport["hgt"][:-2]
    if not h.isnumeric():
        return False
    h = int(h)
    if h_unit == "cm":
        if h < 150 or h > 193:
            return False
    elif h_unit == "in":
        if h < 59 or h > 76:
            return False
    else:
        return False

    if len(passport["hcl"]) != 7:
        return False
    if passport["hcl"][0] != "#":
        return False

    hcl = passport["hcl"][1:]
    if not all(x in "0123456789abcdef" for x in hcl):
        return False

    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    if not passport["pid"].isnumeric():
        return False
    if len(passport["pid"]) != 9:
        return False

    return True


def part1(filename):
    passports = parse_input(filename)
    valid = [passport for passport in passports if is_valid_part1(passport)]
    return len(valid)


def part2(filename):
    passports = parse_input(filename)
    valid = [passport for passport in passports if is_valid_part2(passport)]
    return len(valid)


assert part1(os.path.join(currentdir, "test_input1.txt")) == 2

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))

assert part2(os.path.join(currentdir, "test_input2.txt")) == 0
assert part2(os.path.join(currentdir, "test_input3.txt")) == 4

print("Part 2: ", part2(os.path.join(currentdir, "input.txt")))
