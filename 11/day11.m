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

function new_counts = count_diagonals(counts, state, seat_mask, x, y)
  [maxx, maxy] = size(state);
  directions = [
    1  1 -1 -1;
   -1  1 -1  1
  ];

  for dir = directions
    current_state = state(x, y);
    nx = x + dir(1);
    ny = y + dir(2);
    while nx > 0 && nx <= maxx && ny > 0 && ny <= maxy
      counts(nx, ny) = counts(nx, ny) + current_state;
      if state(nx, ny) == 1
        current_state = 1;
      elseif seat_mask(nx, ny) == 1
        current_state = 0;
      endif
      nx = nx + dir(1);
      ny = ny + dir(2);
    endwhile
  endfor

  new_counts = counts;
endfunction

function counts = count_neighbours(state, seat_mask)
  counts = zeros(size(state));

  [maxx, maxy] = size(state);
  empty_seats = !state .* seat_mask;

  # Horizontal and vertical directions
  row_state = state(1, :);
  for x = 2:maxx
    counts(x, :) = counts(x, :) + row_state;
    row_state = max(row_state, state(x, :));
    row_state = row_state .* !empty_seats(x, :);
  endfor

  row_state = state(maxx, :);
  for x = maxx-1:-1:1
    counts(x, :) = counts(x, :) + row_state;
    row_state = max(row_state, state(x, :));
    row_state = row_state .* !empty_seats(x, :);
  endfor

  row_state = state(:, 1);
  for y = 2:maxy
    counts(:, y) = counts(:, y) + row_state;
    row_state = max(row_state, state(:, y));
    row_state = row_state .* !empty_seats(:, y);
  endfor

  row_state = state(:, maxy);
  for y = maxy-1:-1:1
    counts(:, y) = counts(:, y) + row_state;
    row_state = max(row_state, state(:, y));
    row_state = row_state .* !empty_seats(:, y);
  endfor

  # Diagonals
  for x = 1:maxx
    for y = [1, maxy]
      counts = count_diagonals(counts, state, seat_mask, x, y);
    endfor
  endfor

  for x = [1, maxx]
    for y = 2:maxy-1
      counts = count_diagonals(counts, state, seat_mask, x, y);
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
