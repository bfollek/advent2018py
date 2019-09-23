#!/usr/bin/env python3

from collections import defaultdict
from typing import DefaultDict, Optional, Tuple


def part1(file_name: str) -> int:
    """
    Calculate the checksum.

    To do this count the number of letters that appear exactly twice in an ID,
    and the number of letters that appear exactly three times. Then multiply
    the counts together.
    """
    count_2 = 0
    count_3 = 0
    with open(file_name) as f:
        for line in f:
            id = line.rstrip()
            has_2, has_3 = _check_chars(id)
            if has_2:
                count_2 += 1
            if has_3:
                count_3 += 1
    return count_2 * count_3


def part2(file_name: str) -> Optional[str]:
    """
    Find the 2 id's that differ by just 1 char, and return their common chars.
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
    return None


def _check_chars(id: str) -> Tuple[bool, bool]:
    """
    The first bool is True if any char in id occurs twice.
    The second is True if any char occurs three times.
    """
    d: DefaultDict[str, int] = defaultdict(lambda: 0)
    for c in id:
        d[c] += 1
    counts = d.values()
    return 2 in counts, 3 in counts


def _diff_by_1(id1: str, id2: str) -> Tuple[bool, Optional[str]]:
    """
    If the boolean is True, the string is the chars
    that id1 and id2 have in common.
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
