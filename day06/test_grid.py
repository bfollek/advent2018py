from coordinate import Coordinate
from grid import Grid

# Use the example from day06.spc
A = (1, 1)
B = (1, 6)
C = (8, 3)
D = (3, 4)
E = (5, 5)
F = (8, 9)


def make_grid():
    g = Grid()
    g.add_coordinate(*A)
    g.add_coordinate(*B)
    g.add_coordinate(*C)
    g.add_coordinate(*D)
    g.add_coordinate(*E)
    g.add_coordinate(*F)
    return g


def test_add_coordinate():
    g = make_grid()
    assert g._min_x == 1
    assert g._max_x == 8
    assert g._min_y == 1
    assert g._max_y == 9
    assert len(g.coordinates) == 6


def test_is_finite():
    g = make_grid()
    assert not g.is_finite(g.coordinates[A])
    assert not g.is_finite(g.coordinates[B])
    assert not g.is_finite(g.coordinates[C])
    assert g.is_finite(g.coordinates[D])
    assert g.is_finite(g.coordinates[E])
    assert not g.is_finite(g.coordinates[F])


def test_empty_locations():
    g = make_grid()
    assert A not in g.empty_locations()
    assert C not in g.empty_locations()
    assert E not in g.empty_locations()
    assert (4, 4) in g.empty_locations()
    assert (7, 6) in g.empty_locations()
