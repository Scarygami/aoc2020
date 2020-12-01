# [Day 1: Report Repair](https://adventofcode.com/2020/day/1)

Hand-coded in [IntCode](https://adventofcode.com/2019/day/9), since [my compiler from last year](https://github.com/Scarygami/aoc2019/tree/master/ic_compiler) wasn't really advanced enough to handle this puzzle. Keeping track of all the memory references is a real pain when done manually. The possibility of IntCode to rewrite itself was rather useful to change the references to the correct data locations in the loops.

Can be executed using my [IntCode "VM" from last year](https://github.com/Scarygami/aoc2019/blob/master/lib/intcode.py).

You need to add your puzzle input add the end of files where indicated instead of the sample input.

    python intcode.py path/to/01_part1.ic
    python intcode.py path/to/02_part1.ic
