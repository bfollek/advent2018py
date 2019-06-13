from day03 import part1, part2
from claim import Claim


def test_part1():
    assert part1("day03/day03.dat") == 109716


def test_part2():
    assert part2("day03/day03.dat") == "124"
    print(Claim._sq_inches.cache_info())  # pytest -s to see this


def test_claim_new_from_string():
    s = "#14 @ 690,863: 12x20"
    claim = Claim.new_from_string(s)
    assert claim.id == "14"
    assert claim._x == 690
    assert claim._y == 863
    assert claim._width == 12
    assert claim._height == 20


def test_claim_sq_inches():
    c1 = Claim.new_from_string("#1 @ 1,3: 4x4")
    assert c1.sq_inches == [
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
    c1 = Claim.new_from_string("#1 @ 1,3: 4x4")
    c2 = Claim.new_from_string("#2 @ 3,1: 4x4")
    c3 = Claim.new_from_string("#3 @ 5,5: 2x2")
    c4 = Claim.new_from_string("#4 @ 1,1: 1x1")
    assert c1.overlaps(c2)
    assert c2.overlaps(c1)
    assert c1.overlaps(c3) == False
    assert c4.overlaps(c4)
