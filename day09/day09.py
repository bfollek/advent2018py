#!/usr/bin/env python3

import re

from circle import Circle

# e.g., "468 players; last marble is worth 71843 points"
GAME_REGEX = re.compile(r"(\d+) players; last marble is worth (\d+) points")


def part1(file_name):
    """
    What is the winning Elf's score?
    """
    num_elves, last_marble = map(int, _parse_game(file_name))
    scores = _play_game(num_elves, last_marble)
    return max(scores)


def part2(file_name):
    pass


def _play_game(num_elves, last_marble):
    circle = Circle()
    elf_num = 0
    scores = [0] * num_elves
    for marble_num in range(1, last_marble + 1):
        elf_num = (elf_num + 1) % num_elves
        _move(marble_num, elf_num, circle, scores)
    return scores


def _move(marble_num, elf_num, circle, scores):
    if _is_winner(marble_num):
        _handle_winner(marble_num, elf_num, circle, scores)
    else:
        circle.place(marble_num)


def _is_winner(marble_num):
    """
    if the marble that is about to be placed has a number which is a multiple of 23
    """
    return marble_num % 23 == 0


def _handle_winner(marble_num, elf_num, circle, scores):
    """
    First, the current player keeps the marble they would have placed, adding it to their score. In addition, the marble 7 marbles counter-clockwise from the current marble is removed from the circle and also added to the current player's score. The marble located immediately clockwise of the marble that was removed becomes the new current marble.
    """
    scores[elf_num] += marble_num
    remove_index, remove_value = circle.move(-7)
    scores[elf_num] += remove_value
    del circle[remove_index]
    # Because of deletion, remove_index is now the index immediately clockwise to itself
    circle.current = remove_index


def _parse_game(file_name):
    with open(file_name) as f:
        line = f.read().strip()
    m = re.search(GAME_REGEX, line)
    num_elves, last_marble = m.group(1, 2)
    return (num_elves, last_marble)
