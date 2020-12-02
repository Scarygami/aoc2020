# [Day 2: Password Philosophy](https://adventofcode.com/2020/day/2)

Solved in Excel using the following formulas

| Column | Column Name   | Formula                                             |
| ------ | ------------- | --------------------------------------------------- |
| A      | Input         | Copy & paste of puzzle input                        |
| B      | :             | `=SEARCH(":",[@Input])`                             |
| C      | Rule          | `=MID([@Input],1,[@[:]]-1)`                         |
| D      | MinMax        | `=LEFT([@Rule],LEN([@Rule])-2)`                     |
| E      | -             | `=SEARCH("-",[@MinMax])`                            |
| F      | Min           | `=VALUE(MID([@MinMax],1,[@[-]]-1))`                 |
| G      | Max           | `=VALUE(MID([@MinMax],[@[-]]+1,10))`                |
| H      | Letter        | `=RIGHT([@Rule],1)`                                 |
| I      | PW            | `=MID([@Input],[@[:]]+2,100)`                       |
| J      | Count         | `=LEN([@PW]) - LEN(SUBSTITUTE([@PW],[@Letter],""))` |
| K      | Part 1 valid  | `=AND([@Count]>=[@Min],[@Count]<=[@Max])`           |
| L      | Letter in Min | `=MID([@PW],[@Min],1)=[@Letter]`                    |
| M      | Letter in Max | `=MID([@PW],[@Max],1)=[@Letter]`                    |
| N      | Part 2 valid  | `=XOR([@[Letter in Min]],[@[Letter in Max]])`   |


Formula to get the solution from the table (assuming the table is named AOC):

Part 1: `=COUNTIF(AOC[Part 1 valid],TRUE)`

Part 2: `=COUNTIF(AOC[Part 2 valid],TRUE)`
 

![Excel Screenshot](https://raw.githubusercontent.com/Scarygami/aoc2020/main/02/aoc2020_day2.png)
