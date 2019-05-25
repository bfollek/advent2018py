from day03 import part1, _line_to_claim
from claim import Claim


def test_part1():
    assert part1("day03/day03.txt") == 109716


def test_line_to_claim():
    line = "#14 @ 690,863: 12x20"
    claim = _line_to_claim(line)
    assert claim.id == "14"
    assert claim.x == 690
    assert claim.y == 863
    assert claim.width == 12
    assert claim.height == 20


def test_claim_sq_inches():
    c1 = _line_to_claim("#1 @ 1,3: 4x4")
    assert c1.sq_inches() == [
        (1, 3),
        (1, 4),
        (1, 5),
        (1, 6),
        (2, 3),
        (2, 4),
        (2, 5),
        (2, 6),
        (3, 3),
        (3, 4),
        (3, 5),
        (3, 6),
        (4, 3),
        (4, 4),
        (4, 5),
        (4, 6),
    ]


def test_claim_overlap():
    c1 = _line_to_claim("#1 @ 1,3: 4x4")
    c2 = _line_to_claim("#2 @ 3,1: 4x4")
    c3 = _line_to_claim("#3 @ 5,5: 2x2")
    c4 = _line_to_claim("#4 @ 1,1: 1x1")
    assert c1.overlaps(c2)
    assert c2.overlaps(c1)
    assert c1.overlaps(c3) == False
    assert c4.overlaps(c4)
