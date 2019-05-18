#!/usr/bin/env python3

from itertools import groupby


def part1(file_name):
    """
   Calculate the checksum. Day 2, part 1.

   To do this count the number of letters that appear exactly twice in an ID,
   and the number of letters that appear exactly three times. Then multiply
   the counts together.

    >>> part1('day02.txt')
    8715
    """
    count_2 = 0
    count_3 = 0
    with open(file_name) as f:
        for id in f:
            counts = char_counts(id)
            if 2 in counts:
                count_2 += 1
            if 3 in counts:
                count_3 += 1
    return count_2 * count_3


def char_counts(id):
    """
    Return a list of char counts.

    >>> char_counts('AAAABBBCCDAABBB')
    [6, 6, 2, 1]
    """
    return [len(list(v)) for _, v in groupby(sorted(id))]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
