# [Day 13: Shuttle Search](https://adventofcode.com/2020/day/13)

University math classes finally paying off!

Part 1:

`time_to_wait = id - timestamp mod id`

E.g. for the example, with timestamp 939

| id | calculation                     | time_to_wait |
| -- | ------------------------------- | ------------ |
| 7  | `7 - 939 mod 7 = 7 - 1 = 6`     | 6            |
| 13 | `13 - 939 mod 13 = 13 - 3 = 10` | 10           |
| 59 | `59 - 939 mod 59 = 59 - 54 = 5` | 5            |
| 31 | `31 - 939 mod 31 = 31 - 9 = 22` | 22           |
| 19 | `19 - 939 mod 19 = 19 - 8 = 11` | 11           |

Part 2:

Convert the input to a system of congruences

```
   t     ≡ 0 (mod 7)
   t + 1 ≡ 0 (mod 13)
   t + 4 ≡ 0 (mod 59)
   t + 6 ≡ 0 (mod 31)
   t + 7 ≡ 0 (mod 19)
```

which is equivalent to

```
   t ≡  0 (mod 7)
   t ≡ -1 (mod 13)
   t ≡ -4 (mod 59)
   t ≡ -6 (mod 31)
   t ≡ -7 (mod 19)
```

The way to solve such systems of congruences is using the [Chinese remainder theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem).

While you could do all the steps yourself (I did for the small sample input to check if this was the right way to go), there's a [nice online tool](https://www.dcode.fr/chinese-remainder) that does all the work for you.
