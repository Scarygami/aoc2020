function day11()
  assert(part1("testinput1.txt") == 37)

  answer1 = part1("input.txt")

  assert(part2("testinput1.txt") == 26)

  answer2 = part2("input.txt")
endfunction

function seat_mask = prepare_data(file)
  # This creates a seat mask matrix from the input file
  fd = fopen(file, "r");
  data = [];
  while((line=fgetl(fd)) != -1)
    data = [data; double(line)];
  endwhile
  seat_mask = [data == 76];
endfunction

function result = part1(file)
  seat_mask = prepare_data(file);
  state = zeros(size(seat_mask));
  previous = ones(size(seat_mask));
  while (min(min(state == previous)) == 0)
    previous = state;

    # apply a counting convolution filter over the state
    counts = conv2(state, [1 1 1; 1 0 1; 1 1 1], "same");

    # seats to empty
    empty = counts >= 4;

    # seats that can be taken (including ones that might already be taken)
    take = [counts == 0] .* seat_mask;

    # perform the changes
    state = max(state .* !empty, take);
  end

  # number of occupied sets
  result = sum(sum(state));
endfunction

function counts = count_neighbours(state, seat_mask)
  # This works but needs some serious optimization...
  counts = zeros(size(state));
  directions = [
    0  0  1  1  1 -1 -1 -1;
    1 -1  0  1 -1  0  1 -1
  ];

  [maxx, maxy] = size(state);

  for x = 1:maxx
    for y = 1:maxy
      for dir = directions
        pos = [x,y] + dir';
        while pos(1) > 0 && pos(1) <= maxx && pos(2) > 0 && pos(2) <= maxy
          if state(pos(1), pos(2)) == 1
            counts(x,y) = counts(x,y) + 1;
            break
          endif
          if seat_mask(pos(1), pos(2)) == 1
            break
          endif
          pos = pos + dir';
        endwhile
      endfor
    endfor
  endfor

endfunction

function result = part2(file)
  seat_mask = prepare_data(file);
  state = zeros(size(seat_mask));
  previous = ones(size(seat_mask));

  while (min(min(state == previous)) == 0)
    previous = state;

    # apply a counting convolution filter over the state
    counts = count_neighbours(state, seat_mask);

    # seats to empty
    empty = counts >= 5;

    # seats that can be taken (including ones that might already be taken)
    take = [counts == 0] .* seat_mask;

    # perform the changes
    state = max(state .* !empty, take);
  end

  # number of occupied sets
  result = sum(sum(state));
endfunction
