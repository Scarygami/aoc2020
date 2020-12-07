import argparse
import re

COMMON_CODE = """
use_module(library(lists)).

rec_contains(Parent, Count, Child) :- contains(Parent, Count, Child).
rec_contains(Parent, Count, Child) :-
  contains(Parent, X, Direct_child),
  rec_contains(Direct_child, Y, Child),
  Count is X * Y.

:- findall(X, rec_contains(X, _, shiny_gold), List),
   list_to_set(List, Set),
   length(Set, Part1),
   write('Part 1: '),
   writeln(Part1).


:- findall(X, rec_contains(shiny_gold, X, _), List),
   sum_list(List, Part2),
   write('Part 2: '),
   writeln(Part2).

"""


def create_facts(filename):
    lines = []
    facts = []
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    for line in lines:
        matches = re.search("([a-z ]+) bags contain (.+)", line)
        if matches is None:
            continue

        if matches[2] == "no other bags.":
            continue

        parent = matches[1].replace(" ", "_")
        children = matches[2][:-1].split(", ")
        for child in children:
            matches = re.search("([0-9]+) ([a-z ]+) bags?", child)
            child_name = matches[2].replace(" ", "_")
            facts.append(f"contains({parent}, {matches[1]}, {child_name}).")

    return facts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Puzzle input from Advent of Code 2020 / Day 7")
    parser.add_argument(
        "output", help="Generated output file in Prolog (will be overwritten)"
    )
    args = parser.parse_args()

    if args.input == args.output:
        parser.error("Input and output have to be different files")
        return

    facts = create_facts(args.input)

    with open(args.output, "w") as f:
        f.write("\n".join(facts) + "\n\n")
        f.write(COMMON_CODE)


if __name__ == "__main__":
    main()
