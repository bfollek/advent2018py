#!/usr/bin/env python3

import re

from data_structures.simple_graph.graph import Digraph, Edge
from step import Step, TimedStep

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
        _add_step_to_graph(line, dg, Step)
    # dg.dump()
    steps = _order(dg)
    return "".join([st.name for st in steps])


def part2(file_name, num_workers):
    """
    With 5 workers and the 60+ second step durations (see spec.txt),
    how long will it take to complete all of the steps?
    """
    dg = Digraph()
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]
    for line in lines:
        _add_step_to_graph(line, dg, TimedStep)
    return _how_long(dg, num_workers)


def _add_step_to_graph(line, dg, klass):
    m = re.search(STEP_REGEX, line)
    if m:
        step1, step2 = map(klass, m.group(1, 2))
        for v in [step1, step2]:
            if v not in dg.vertices:
                dg.add_vertex(v)
        # Edge from step2 to step1 because step2 depends on step1
        dg.add_edge_by_vertices(step2, step1)
    else:
        raise ValueError(f"Can't parse [{line}]")


def _order(dg):
    """
    If more than one step is ready, choose the step which is first alphabetically.
    """
    # Dictionary because a set doesn't preserve key order.
    completed = {}
    # A vertex == a step. Loop till all steps are completed.
    while len(completed) < dg.vertex_count:
        # Find all steps that are runnable because their dependencies have completed.
        runnable = []
        for step in dg.vertices:
            if step in completed:
                continue
            dependencies = set(dg.neighbors_for_vertex(step))
            if dependencies.issubset(set(completed)):
                runnable.append(step)
        if runnable:
            # If multiple steps are ready to run, choose whichever is first in alpha order.
            next = sorted(runnable)[0]
            completed[next] = True
    return completed


def _how_long(dg, num_workers):
    clock = 0
    running = set()
    while True:
        runnable = []
        for step in dg.vertices:
            if step.completed(clock):
                if step in running:
                    running.remove(step)
                continue
            if step not in running:
                dependencies = dg.neighbors_for_vertex(step)
                if all(d.completed(clock) for d in dependencies):
                    runnable.append(step)
            _run_steps(runnable, running, num_workers, clock)
        # If nothing's running, we're done
        if not running:
            break
        clock += 1
    return clock


def _run_steps(runnable, running, num_workers, clock):
    # If multiple steps are runnable, run in alpha order.
    runnable.sort()
    i = 0
    while len(running) < num_workers and i < len(runnable):
        nxt = runnable[i]
        nxt.start(clock)
        running.add(nxt)
        i += 1
