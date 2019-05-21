#!/usr/bin/env python3


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
        for line in f:
            id = line.rstrip("\n")
            has_2, has_3 = _check_chars(id)
            if has_2:
                count_2 += 1
            if has_3:
                count_3 += 1
    return count_2 * count_3


def _check_chars(id):
    """
    Return a tuple of two booleans. The first is True if any char in id occurs twice.
    The second is True if any char occurs three times.

    >>> _check_chars('AAAABBBCCDAABBB')
    (True, False)
    >>> _check_chars('AAAABBCCDAAB')
    (True, True)
    >>> _check_chars('AACCAABBCDAAB')
    (False, True)
    >>> _check_chars('AACAABBCCDABACB')
    (False, False)
    """
    d = {}
    for c in id:
        if d.get(c):
            d[c] += 1
        else:
            d[c] = 1
    counts = d.values()
    return 2 in counts, 3 in counts


def part2(file_name):
    """
    Find the 2 id's that differ by just 1 char, and return their common chars.

    >>> part2('day02.txt')
    'fvstwblgqkhpuixdrnevmaycd'
    """
    ids = []
    with open(file_name) as f:
        for line in f:
            id = line.rstrip("\n")
            ids.append(id)
    for id1 in ids:
        for id2 in ids:
            (b, common_chars) = _diff_by_1(id1, id2)
            if b:
                return common_chars


def _diff_by_1(id1, id2):
    """
    Return a tuple (boolean, string). If the boolean is True,
    the string is the chars that id1 and id2 have in common.

    >>> _diff_by_1('ABCD', 'ABCX')
    (True, 'ABC')
    >>> _diff_by_1('AZBCD', 'APBCX')[0]
    False
    >>> _diff_by_1('ABCD', 'ABCD')[0]
    False
    >>> _diff_by_1('ABCDE', 'ABCD')[0]
    False
    >>> _diff_by_1('ABCD', 'ABCD')[0]
    False
    """
    if (id1 == id2) or (len(id1) != len(id2)):
        return False, ""
    diffs = 0
    common_chars = ""
    for i, _ in enumerate(id1):
        if id1[i] != id2[i]:
            diffs += 1
            if diffs > 1:
                return False, ""
        else:
            common_chars += id1[i]
    return True, common_chars


if __name__ == "__main__":
    import doctest

    doctest.testmod()
