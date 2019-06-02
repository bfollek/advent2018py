from coordinate import Coordinate
from plane import Plane


def make_plane():
    p = Plane()
    c1 = p.add_coordinate(1, 2)
    c2 = p.add_coordinate(10, 20)
    c3 = p.add_coordinate(100, 200)
    return (p, c1, c2, c3)


def test_construction():
    p, _, _, _ = make_plane()
    assert p._min_x == 1
    assert p._max_x == 100
    assert p._min_y == 2
    assert p._max_y == 200
    assert len(p.coordinates) == 3


def test_is_infinite():
    p, c1, c2, c3 = make_plane()
    assert p.is_infinite(c1)
    assert not p.is_infinite(c2)
    assert p.is_infinite(c3)


def test_is_finite():
    p, c1, c2, c3 = make_plane()
    assert not p.is_finite(c1)
    assert p.is_finite(c2)
    assert not p.is_finite(c3)


def test_empty_locations():
    p, c1, c2, c3 = make_plane()
    assert (c1.x, c1.y) not in p.empty_locations()
    assert (c2.x, c2.y) not in p.empty_locations()
    assert (c3.x, c3.y) not in p.empty_locations()
    assert (4, 4) in p.empty_locations()
    assert (55, 55) in p.empty_locations()
