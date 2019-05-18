from .. import fibonacci


def test_sample():
    generator = fibonacci.fibonacci()
    assert [next(generator) for i in range(10)] == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_sum():
    generator = fibonacci.fibonacci()
    assert sum(next(generator) for i in range(10)) == 231


def test_even_sum():
    generator = fibonacci.fibonacci()
    assert sum(i for i in fibonacci.even_fibonacci_up_to(generator, 90)) == 44


def test_final():
    generator = fibonacci.fibonacci()
    assert sum(i for i in fibonacci.even_fibonacci_up_to(generator, 4 * 10**6)) == 4613732
