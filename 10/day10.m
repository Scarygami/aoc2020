function day10()
  pkg load statistics;

  assert(part1("testinput1.txt") == 35)
  assert(part1("testinput2.txt") == 220)

  answer1 = part1("input.txt")

  assert(part2("testinput1.txt") == 8)
  assert(part2("testinput2.txt") == 19208)

  answer2 = part2("input.txt")
endfunction

function data = prepare_data(file)
  # This sorts the puzzle input and attaches the 0-jolt outlet and the adapter
  input = dlmread(file);
  sorted = sort(input);
  data = [0;sorted;max(sorted)+3];
endfunction

function result = part1(file)
  data = prepare_data(file);

  # Shift the input vectors to calculate the jolt differences
  differences = data(2:end) - data(1:end - 1);

  result = sum(differences == 3) * sum(differences == 1);
endfunction

function result = part2(file)
  data = prepare_data(file);

  differences = pdist2(data, data, "L1");

  # This matrix describes which adapters can be connected to each other
  reachability = differences >= 1 & differences <= 3;

  # Paths will contain the number of ways to get to the each adapter
  paths = zeros(size(data));
  paths(1) = 1;
  for i = 2:size(data)
    # mask for the nodes that can come before
    possible_origins = reachability(1:i-1, i);

    # number of possible paths to reach those nodes
    possible_paths = paths(1:i-1);

    # element-wise multiplication to only pick the paths to possible origins.
    paths(i) = sum(possible_origins .* possible_paths);
  endfor

  result = max(paths);
endfunction
