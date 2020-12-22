import os
import itertools

currentdir = os.path.dirname(os.path.abspath(__file__))


def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    foods = []
    for line in lines:
        ingredients, allergens = line[:-1].split(" (contains ")
        foods.append((ingredients.split(" "), allergens.split(", ")))

    return foods


def part1(filename):
    foods = parse_input(filename)

    allergens = {}

    for food in foods:
        for allergen in food[1]:
            if allergen in allergens:
                allergens[allergen].intersection_update(food[0])
            else:
                allergens[allergen] = set(food[0])

    allergen_ingredients = set(itertools.chain(*allergens.values()))

    return sum(
        sum(1 for ingredient in food[0] if ingredient not in allergen_ingredients)
        for food in foods
    )


def part2(filename):
    foods = parse_input(filename)

    allergens = {}

    for food in foods:
        for allergen in food[1]:
            if allergen in allergens:
                allergens[allergen].intersection_update(food[0])
            else:
                allergens[allergen] = set(food[0])

    ingredients = set(itertools.chain(*allergens.values()))
    unique = [
        list(ingredients)[0]
        for ingredients in allergens.values()
        if len(ingredients) == 1
    ]

    while len(unique) != len(ingredients):
        for allergen in allergens:
            if len(allergens[allergen]) > 1:
                allergens[allergen].difference_update(unique)

        unique = [
            list(ingredients)[0]
            for ingredients in allergens.values()
            if len(ingredients) == 1
        ]

    dangerous = []
    for allergen in sorted(allergens.keys()):
        dangerous.append(list(allergens[allergen])[0])

    return ",".join(dangerous)


assert part1(os.path.join(currentdir, "testinput1.txt")) == 5

print("Part 1: ", part1(os.path.join(currentdir, "input.txt")))

assert part2(os.path.join(currentdir, "testinput1.txt")) == "mxmxvkd,sqjhc,fvjkl"

print("Part 2: ", part2(os.path.join(currentdir, "input.txt")))
