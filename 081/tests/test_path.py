import pytest

from path import path


test_matrix = [[131, 201, 630, 537, 805],
               [673, 96, 803, 699, 732],
               [234, 342, 746, 497, 524],
               [103, 965, 422, 121, 37],
               [18, 150, 111, 956, 331]]


def test_matrix_cut_small():
    assert path.matrix_cut(test_matrix, 2) == [673, 201]


def test_matrix_cut_big():
    assert path.matrix_cut(test_matrix, 7) == [111, 121, 524]


def test_matrix_cut_over():
    with pytest.raises(ValueError):
        path.matrix_cut(test_matrix, 16)
