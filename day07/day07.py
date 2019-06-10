#!/usr/bin/env python3

import re

from data_structures.simple_graph.graph import Digraph, Edge

# Step P must be finished before step O can begin.
STEP_REGEX = re.compile(r"Step (.*) must be finished before step (.*) can begin.")


def part1(file_name):
    """
    Your first goal is to determine the order in which the steps should be completed.
    """
    dg = Digraph()
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    for line in lines:
        _add_line_to_graph(line, dg)
    # dg.dump()
    order = _determine_order(dg)
    return "".join(order)


def part2(file_name):
    pass


def _add_line_to_graph(line, dg):
    m = re.search(STEP_REGEX, line)
    if m:
        step1, step2 = m.group(1, 2)
        for v in [step1, step2]:
            if v not in dg.vertices:
                dg.add_vertex(v)
        # Edge from step2 to step1 because step2 depends on step1
        dg.add_edge_by_vertices(step2, step1)
    else:
        raise ValueError(f"Can't parse [{line}]")


def _determine_order(dg):
    """
    If more than one step is ready, choose the step which is first alphabetically.
    """
    # Dictionary because a set doesn't preserve key order.
    completed = {}
    # A vertex == a step. Loop till all steps are completed.
    while len(completed) < dg.vertex_count:
        # Find all steps that are ready to run because their dependencies have completed.
        ready_to_run = []
        for step in dg.vertices:
            if step in completed:
                pass
            else:
                dependencies = set(dg.neighbors_for_vertex(step))
                if dependencies.issubset(set(completed)):
                    ready_to_run.append(step)
        if ready_to_run:
            # If multiple steps are ready to run, choose whichever is first in alpha order.
            next = sorted(ready_to_run)[0]
            completed[next] = True
    return completed
