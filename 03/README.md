# [Day 3: Toboggan Trajectory](https://adventofcode.com/2020/day/3)

JS to be executed directly in browser console, i.e. open your input in browser, open developer tools, and past this into the console (only tested in Chrome)

Part 1:
```
{
  const lines = document.body.textContent.split('\n');
  const width = lines[0].length;
  const height = lines.length;
  let x = 0;
  let y = 0;
  let trees = 0;

  while (y < height) {
    if (lines[y][x] === '#') {
      trees = trees + 1;
    }
    y = y + 1
    x = (x + 3) % width;
  }
  console.log('Part 1: ', trees);
}
```

Part 2:
```
{
  const lines = document.body.textContent.split('\n');
  const width = lines[0].length;
  const height = lines.length;
  const directions = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]];
  let total = 1;

  directions.forEach(([dx, dy]) => {
    let x = 0;
    let y = 0;
    let trees = 0;
    while (y < height) {
      if (lines[y][x] === '#') {
        trees = trees + 1;
      }
      y = y + dy;
      x = (x + dx) % width;
    }
    total = total * trees;
  });
  console.log('Part 2: ', total);
}
```
