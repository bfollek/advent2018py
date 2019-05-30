#!/usr/bin/env python3

import re


def part1(file_name):
    """
    Strategy 1: Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?

    What is the ID of the guard you chose multiplied by the minute you chose?
    """
    return 0


def part2(file_name):
    """
    Strategy 2: Of all guards, which guard is most frequently asleep on the same minute?

    What is the ID of the guard you chose multiplied by the minute you chose?
    """
    return 0


# array.array for minutes
# list of naps
# Nap class
# guard
# (start, end) arrays
# CLAIM_REGEX = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
# m = re.search(cls.CLAIM_REGEX, s)
#         flds = list(m.groups())
#         # Convert to int where necessary
#         for i in range(1, len(flds)):
#             flds[i] = int(flds[i])
#         return Claim(*flds)

BEGINS_SHIFT_REGEX = re.compile(r".*Guard #(\d+) begins shift")
FALLS_ASLEEP_REGEX = re.compile(r".*:(\d+)] falls asleep")
WAKES_UP_REGEX = re.compile(r".*:(\d+)] wakes up")


def _parse_line(line):
    """
  Parse lines like these:

  [1518-11-01 00:00] Guard #10 begins shift
  [1518-11-01 00:05] falls asleep
  [1518-11-01 00:25] wakes up
  """
    pass
