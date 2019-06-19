#!/usr/bin/env python3

from collections import deque

from node import Node


def part1(file_name):
    """
    What is the sum of all metadata entries?
    """
    with open(file_name) as f:
        raw = f.readline().strip()
    dek = deque(int(s) for s in raw.split(" "))
    # print(dek)
    node = _parse_node(dek)
    # print(node)
    return node.total_metadata


def part2(file_name):
    pass


def _parse_node(data):
    num_children = data.popleft()
    num_metadata = data.popleft()
    node = Node()
    for _ in range(num_children):
        node.add_child(_parse_node(data))
    for _ in range(num_metadata):
        node.add_metadata(data.popleft())
    return node
