def read_matrix_from_file(file_name):
    with open(file_name, 'r') as infile:
        lines = infile.read().splitlines()

    return list(list(map(int, line.split(","))) for line in lines)
