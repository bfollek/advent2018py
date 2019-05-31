#!/usr/bin/env python3

from collections import defaultdict
import re


def part1(file_name):
    """
    How many units remain after fully reacting the polymer you scanned?
    """
    with open(file_name) as f:
        polymer = f.readline().rstrip()
    reacted = _react(polymer)
    return len(reacted)


def part2(file_name):
    """
    Your goal is to figure out which unit type is causing the most problems, remove all instances of it (regardless of polarity), fully react the remaining polymer, and measure its length.

    What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?
    """
    with open(file_name) as f:
        polymer = f.readline().rstrip()
    d = {}
    for c in polymer:
        c = c.upper()  # Ignore case
        if not c in d:  # Check each char just once
            s = _remove(c, polymer)
            d[c] = len(_react(s))
    return min(d.values())


def _react(polymer):
    reacted = []
    for c in polymer:
        # If reacted has a last char and it reacts with c, drop the last char.
        if len(reacted) > 0 and _reacts_with(c, reacted[-1]):
            reacted.pop()
        else:
            reacted.append(c)
    return "".join(reacted)


def _reacts_with(a, b):
    # True if a and b differ only in case
    return (a != b) and (a.upper() == b.upper())


def _remove(c, polymer):
    return re.sub(c, "", polymer, flags=re.IGNORECASE)
