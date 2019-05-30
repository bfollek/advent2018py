#!/usr/bin/env python3

from collections import defaultdict

from claim import Claim

NOT_FOUND = "Could not find claim that doesn't overlap any other claim."


def part1(file_name):
    """
    How many square inches of fabric are within two or more claims?
    """
    with open(file_name) as f:
        claims = [Claim.new_from_string(line.rstrip()) for line in f]
    d = defaultdict(lambda: 0)
    # Count how many times each square inch appears in a claim
    for claim in claims:
        for sq_inch in claim.sq_inches():
            d[sq_inch] += 1
    # Count the # of values in d that are > 1
    return len([v for v in d.values() if v > 1])


def part2(file_name):
    return part2_v2(file_name)


def part2_v1(file_name):
    """
    Find the one claim that doesn't overlap any other claim. Return its id.
    """
    with open(file_name) as f:
        claims = [Claim.new_from_string(line.rstrip()) for line in f]
    for claim in claims:
        if _no_overlap(claim, claims):
            return claim.id
    raise NOT_FOUND


def _no_overlap(claim, claims):
    for other in claims:
        if claim == other:
            continue
        if claim.overlaps(other):
            return False
    return True


def part2_v2(file_name):
    """
    Find the one claim that doesn't overlap any other claim. Return its id.

    This version is much faster than part2_v1().
    """
    with open(file_name) as f:
        claims = [Claim.new_from_string(line.rstrip()) for line in f]
    # Each key is a claim ID. Each value is a bool.
    d_claim_ids = {}
    # Each key is a sq inch tuple. Each value is a list of claim ID's.
    d_sq_inches = defaultdict(list)
    # Load both dictionaries. d_claim_ids will end up with all claim ID's.
    # d_sq_inches will end up with all square inches that have claims on them,
    # and a list of the claim ID's that have the claims.
    for claim in claims:
        d_claim_ids[claim.id] = True
        for sq_inch in claim.sq_inches():
            d_sq_inches[sq_inch].append(claim.id)
    # Now for all square inches with more than one claim,
    # flip d_claim_ids_no_overlap to False.
    for claim_list in d_sq_inches.values():
        if len(claim_list) > 1:
            for claim_id in claim_list:
                d_claim_ids[claim_id] = False
    # Now return the one claim ID that's still True.
    for claim_id, b in d_claim_ids.items():
        if b:
            return claim_id
    raise NOT_FOUND


def part2_v3(file_name):
    """
    Find the one claim that doesn't overlap any other claim. Return its id.

    This version is similar to part2_v2(), but we handle the filtering of the
    claim ID's differently. In my haphazard benchmarking, it seems marginally
    slower.
    """
    with open(file_name) as f:
        claims = [Claim.new_from_string(line.rstrip()) for line in f]
    # Each value is a claim ID.
    set_claim_ids = set()
    # Each key is a sq inch tuple. Each value is a list of claim ID's.
    d_sq_inches = defaultdict(list)
    # set_claim_ids will end up with all claim ID's.
    # d_sq_inches will end up with all square inches that have claims on them,
    # and a list of the claim ID's that have the claims.
    for claim in claims:
        set_claim_ids.add(claim.id)
        for sq_inch in claim.sq_inches():
            d_sq_inches[sq_inch].append(claim.id)
    # Now for all square inches with more than one claim,
    # discard the claim ID's from set_claim_ids.
    for claim_list in d_sq_inches.values():
        if len(claim_list) > 1:
            for claim_id in claim_list:
                set_claim_ids.discard(claim_id)
    # The only claim ID left is one we want.
    return set_claim_ids.pop()
