#!/usr/bin/env python3

from itertools import cycle


def part1(file_name):
    """
    Find the total of the frequencies.
    """
    with open(file_name) as f:
        freqs = [int(line.rstrip()) for line in f]
    return sum(freqs)


def part2(file_name):
    """
    Keep a running total, and find the first value that repeats.
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
