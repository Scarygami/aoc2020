# [Day 15: Rambunctious Recitation](https://adventofcode.com/2020/day/15)

Part 1 done in J:

    previous =: _1 & }.
    last =: _1 & {
    index =: (previous i: last)
    age =: - & 1 @: (# - index)
    result =: (, age)
    turns =: 2020 & - @: #
    part1 =: (_1 { (result ^: turns))

or

    part1=:_1{(,-&1@:#-_1&}.i:_1&{)^:(2020&-@:#)

       part1 0,3,6
    436
