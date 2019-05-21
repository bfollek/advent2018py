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
        ids = [line.rstrip() for line in f]
    for id in ids:
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
        # If necessary, add c to d, with value of 0
        d.setdefault(c, 0)
        d[c] += 1
    counts = d.values()
    return 2 in counts, 3 in counts


def part2(file_name):
    """
    Find the 2 id's that differ by just 1 char, and return their common chars.

    >>> part2('day02.txt')
    'fvstwblgqkhpuixdrnevmaycd'
    """
    with open(file_name) as f:
        ids = [line.rstrip() for line in f]
    for i, id1 in enumerate(ids):
        for j, id2 in enumerate(ids):
            # If i == j, id1 == id2
            if i != j:
                b, common_chars = _diff_by_1(id1, id2)
                if b:
                    return common_chars


def _diff_by_1(id1, id2):
    """
    Return a tuple (boolean, string). If the boolean is True,
    the string is the chars that id1 and id2 have in common.

    >>> _diff_by_1('ABCD', 'ABCX')
    (True, 'ABC')
    >>> _diff_by_1('AZBCD', 'APBCX')
    (False, None)
    >>> _diff_by_1('ABCD', 'ABCD') # Same string
    (False, None)
    >>> _diff_by_1('ABCDE', 'ABCD') # Different lengths
    (False, None)
    """
    if len(id1) != len(id2):
        return False, None
    diffs = 0
    common_chars = ""
    for i, _ in enumerate(id1):
        if id1[i] != id2[i]:
            diffs += 1
            if diffs > 1:
                break  # No need to continue
        else:
            common_chars += id1[i]
    if diffs == 1:
        return True, common_chars
    else:
        return False, None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
