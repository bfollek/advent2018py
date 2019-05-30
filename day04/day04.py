#!/usr/bin/env python3

from array import array
from collections import defaultdict
import re

from nap import Nap


def part1(file_name):
    """
    Strategy 1: Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?

    What is the ID of the guard you chose multiplied by the minute you chose?
    """
    naps = _file_to_naps(file_name)
    nap_map = _map_naps(naps)
    # Find the guard that has the most minutes asleep.
    most_id = None
    most_minutes = -1
    for id, minutes in nap_map.items():
        tots = sum(minutes)
        if tots > most_minutes:
            most_minutes = tots
            most_id = id
    # What minute does that guard spend asleep the most?
    minutes = nap_map[most_id]
    return int(most_id) * minutes.index(max(minutes))


def part2(file_name):
    """
    Strategy 2: Of all guards, which guard is most frequently asleep on the same minute?

    What is the ID of the guard you chose multiplied by the minute you chose?
    """
    naps = _file_to_naps(file_name)
    nap_map = _map_naps(naps)
    # Which guard is most frequently asleep on the same minute?
    most_id = None
    most_minutes = -1
    most_index = -1
    for id, minutes in nap_map.items():
        maxy = max(minutes)
        if maxy > most_minutes:
            most_minutes = maxy
            most_index = minutes.index(maxy)
            most_id = id
    return int(most_id) * most_index


# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
BEGINS_SHIFT_REGEX = re.compile(r".*Guard #(\d+) begins shift")
FALLS_ASLEEP_REGEX = re.compile(r".*:(\d+)] falls asleep")
WAKES_UP_REGEX = re.compile(r".*:(\d+)] wakes up")


def _file_to_naps(file_name):
    with open(file_name) as f:
        lines = sorted([line.rstrip() for line in f])
    naps = []
    for line in lines:
        m = re.search(BEGINS_SHIFT_REGEX, line)
        if m:
            current_id = m.group(1)
            continue
        m = re.search(FALLS_ASLEEP_REGEX, line)
        if m:
            nap = Nap(current_id, int(m.group(1)))
            continue
        m = re.search(WAKES_UP_REGEX, line)
        if m:
            nap.awake = int(m.group(1))
            naps.append(nap)
            continue
        raise Exception(f"Unexpected line: {line}")
    return naps


def _map_naps(naps):
    # Default value is an array of 60 zeros, a counter for each minute in the hour
    map = defaultdict(lambda: array("B", [0] * 60))
    for nap in naps:
        # For each minute the guard napped, increment the counter
        for i in range(nap.asleep, nap.awake):
            map[nap.id][i] += 1
    return map
