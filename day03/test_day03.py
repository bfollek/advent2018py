from day03 import part1, _line_to_claim


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
