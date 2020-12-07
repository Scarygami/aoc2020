contains(light_red, 1, bright_white).
contains(light_red, 2, muted_yellow).
contains(dark_orange, 3, bright_white).
contains(dark_orange, 4, muted_yellow).
contains(bright_white, 1, shiny_gold).
contains(muted_yellow, 2, shiny_gold).
contains(muted_yellow, 9, faded_blue).
contains(shiny_gold, 1, dark_olive).
contains(shiny_gold, 2, vibrant_plum).
contains(dark_olive, 3, faded_blue).
contains(dark_olive, 4, dotted_black).
contains(vibrant_plum, 5, faded_blue).
contains(vibrant_plum, 6, dotted_black).


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

