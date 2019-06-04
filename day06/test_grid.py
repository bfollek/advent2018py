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
    g.add_coordinate(A)
    g.add_coordinate(B)
    g.add_coordinate(C)
    g.add_coordinate(D)
    g.add_coordinate(E)
    g.add_coordinate(F)
    return g


def test_add_coordinate():
    g = make_grid()
    assert len(g._coord_dict) == 6


def test_empty_locations():
    g = make_grid()
    assert A not in g._empty_locations()
    assert C not in g._empty_locations()
    assert E not in g._empty_locations()
    assert (4, 4) in g._empty_locations()
    assert (7, 6) in g._empty_locations()
