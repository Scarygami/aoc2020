# [Day 5: Binary Boarding](https://adventofcode.com/2020/day/5)

Solved mostly manual in Visual Studio Code.

1.  Copy & paste your input into a new file.
2.  Convert to binary numbers because that's what they are.

    Search & Replace:

        F > 0
        B > 1
        R > 1
        L > 0

3.  Sort the lines "alphabetically" to find the highest number.

    Ctrl+A > Ctrl+Shift+P > Sort Lines Ascending

4.  Scroll to the very bottom and convert the last number to decimal to get the answer for part 1.

5.  For part 2 we are first going to split the lines into blocks according to the rows.
    Add new lines before seat 0 and after seat 7 in each row (in case we have a window seat)

    Search and Replace:

        ([0-9]{7}000) > \n$1
        ([0-9]{7}111) > $1\n

6.  Then we are searching for the block that has only 7 seats instead of 8

        \n\n([0-9]{10}\n){7}\n

7.  Find the missing number in the highlighted block and convert to decimal for the answer to part 2.
