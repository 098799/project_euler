def matrix_cut(matrix, n):
    matrix_length = len(matrix)
    if n < 2*matrix_length:
        return [matrix[n-i-1][i] for i in range(n) if (n-i-1 < matrix_length and i < matrix_length)]
    else:
        raise ValueError("Too big for this matrix")
