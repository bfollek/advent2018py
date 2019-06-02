from coordinate import Coordinate
from grid import Grid


def make_grid():
    g = Grid()
    c1 = g.add_coordinate(1, 2)
    c2 = g.add_coordinate(10, 20)
    c3 = g.add_coordinate(100, 200)
    return (g, c1, c2, c3)


def test_add_coordinate():
    g, _, _, _ = make_grid()
    assert g._min_x == 1
    assert g._max_x == 100
    assert g._min_y == 2
    assert g._max_y == 200
    assert len(g.coordinates) == 3


def test_is_finite():
    g, c1, c2, c3 = make_grid()
    assert not g.is_finite(c1)
    assert g.is_finite(c2)
    assert not g.is_finite(c3)


def test_empty_locations():
    g, c1, c2, c3 = make_grid()
    assert (c1.x, c1.y) not in g.empty_locations()
    assert (c2.x, c2.y) not in g.empty_locations()
    assert (c3.x, c3.y) not in g.empty_locations()
    assert (4, 4) in g.empty_locations()
    assert (55, 55) in g.empty_locations()
