def matrix_cut(matrix, n):
    matrix_length = len(matrix)
    if n < matrix_length:
        return [matrix[n-i-1][i] for i in range(n)]
    elif (n >= matrix_length and n <= 2*len(matrix)-1):
        return [matrix[n-i-1][i] for i in range(n) if (n-i-1 < matrix_length and i < matrix_length)]
    else:
        raise ValueError("Too big for this matrix")

def check_example():
    matrix = [[131, 201, 630, 537, 805],
              [673, 96, 803, 699, 732],
              [234, 342, 746, 497, 524],
              [103, 965, 422, 121, 37],
              [18, 150, 111, 956, 331]]
    print(matrix_cut(matrix, 9))

check_example()
