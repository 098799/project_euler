def fibonacci():
    a, b = 1, 2
    yield a

    while True:
        a, b = b, a + b
        yield a


def even_fibonacci_up_to(generator, threshold):
    result = []

    value = next(generator)

    while value < threshold:
        if value % 2 == 0:
            result.append(value)

        value = next(generator)

    return result
