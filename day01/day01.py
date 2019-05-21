#!/usr/bin/env python3

from itertools import cycle


def part1(file_name):
    """
    Find the total of the frequencies. Day 1, part 1.

    >>> part1('day01.txt')
    592
    """
    with open(file_name) as f:
        freqs = [int(line.rstrip()) for line in f]
    return sum(freqs)


def part2(file_name):
    """
    Keep a running total, and find the first value that repeats.
    Day 1, part 2.

    >>> part2('day01.txt')
    241
    """
    total = 0
    seen = {total}  # seen is a set
    with open(file_name) as f:
        freqs = [int(line.rstrip()) for line in f]
    # cycle() because we may have to loop through freqs
    # more than once before the running total repeats.
    for freq in cycle(freqs):
        total += freq
        if total in seen:
            return total
        else:
            seen.add(total)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
