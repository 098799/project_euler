from .. import multiples


def test_example():
    assert multiples.sum_of_multiples(3, 5, 10) == 23


def test_final():
    assert multiples.sum_of_multiples(3, 5, 1000) == 233168
