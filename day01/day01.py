#!/usr/bin/env python3

from itertools import cycle


def part1(file_name):
    """
    Find the total of the frequencies. Day 1, part 1.

    >>> part1('day01.txt')
    592
    """
    total = 0
    with open(file_name) as f:
        for line in f:
            s = line.rstrip("\n")
            total += int(s)
    return total


def part2(file_name):
    """
    Keep a running total, and find the first value that repeats.
    Day 1, part 2.

    >>> part2('day01.txt')
    241
    """
    freqs = []
    with open(file_name) as f:
        for line in f:
            s = line.rstrip("\n")
            freqs.append(int(s))
    total = 0
    seen = {total}  # seen is a set
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
