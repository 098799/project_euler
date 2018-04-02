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


def test_add_path_small():
    prev_cut = path.matrix_cut(test_matrix, 1)
    next_cut = path.matrix_cut(test_matrix, 2)
    assert path.add_path(prev_cut, next_cut) == [673+131, 201+131]


def test_add_path_big():
    prev_cut = path.matrix_cut(test_matrix, 7)
    next_cut = path.matrix_cut(test_matrix, 8)
    assert path.add_path(prev_cut, next_cut) == [956+111, 37+121]


def test_go_over():
    assert path.go_over(test_matrix) == [2427]


def test_final():
    with open("tests/matrix.txt") as infile:
        raw_input_matrix = infile.read()
    big_matrix = []
    for line in (raw_input_matrix.split("\n"))[:-1]:
        big_matrix.append(line.split(","))

    for n1, line in enumerate(big_matrix):
        for n2, item in enumerate(line):
            big_matrix[n1][n2] = int(item)

    print(path.go_over(big_matrix))  # Final project Euler answer is 427337.
