#!/usr/bin/env python3

import re

# e.g., "468 players; last marble is worth 71843 points"
GAME_REGEX = re.compile(r"(\d+) players; last marble is worth (\d+) points")


def part1(file_name):
    num_players, last_marble = _parse_game(file_name)
    print(num_players, last_marble)


def part2(file_name):
    pass


def _parse_game(file_name):
    with open(file_name) as f:
        line = f.read().strip()
    m = re.search(GAME_REGEX, line)
    num_players, last_marble = m.group(1, 2)
    return (num_players, last_marble)
