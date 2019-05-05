def matrix_cut(matrix, n):
    matrix_length = len(matrix)
    if n < 2*matrix_length:
        return [matrix[n-i-1][i] for i in range(n) if (n-i-1 < matrix_length and i < matrix_length)]
    else:
        raise ValueError("Too big for this matrix")


def add_path(previous_cut, next_cut):
    if len(next_cut) > len(previous_cut):
        borders_enabled = True
        offset = -1
    else:
        borders_enabled = False
        offset = +1
    for number, item in enumerate(next_cut):
        if (number == 0 and borders_enabled):
            next_cut[number] += previous_cut[number]
        elif (number == len(next_cut)-1 and borders_enabled):
            next_cut[number] += previous_cut[-1]
        else:
            next_cut[number] += min(previous_cut[number], previous_cut[number+offset])
    return next_cut


def go_over(matrix):
    prev_cut = matrix_cut(matrix, 1)
    for number in range(2, 2*len(matrix)):
        next_cut = matrix_cut(matrix, number)
        prev_cut = add_path(prev_cut, next_cut)
    return next_cut
