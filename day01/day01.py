#!/usr/bin/env python3


def part1(file_name):
    """
    Day 1, part 1

    >>> part1('day01.txt')
    592
    """
    freqs = [int(line) for line in open(file_name)]
    return sum(freqs)


def part2(file_name):
    """
    Day 1, part 2

    >>> part2('day01.txt')
    241
    """
    from itertools import cycle

    total = 0
    seen = {total}  # seen is a set
    freqs = [int(line) for line in open(file_name)]
    for f in cycle(freqs):
        total += f
        if total in seen:
            return total
        else:
            seen.add(total)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
