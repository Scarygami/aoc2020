contains(shiny_gold, 2, dark_red).
contains(dark_red, 2, dark_orange).
contains(dark_orange, 2, dark_yellow).
contains(dark_yellow, 2, dark_green).
contains(dark_green, 2, dark_blue).
contains(dark_blue, 2, dark_violet).


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

