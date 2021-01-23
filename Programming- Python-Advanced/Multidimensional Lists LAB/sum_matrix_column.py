def read_matrix():
    rows_count, column_count = map(int, input().split(", "))
    matrix = []
    for row_index in range(rows_count):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def column_sum(matrix):
    rows_count = len(matrix)
    column_count = len(matrix[0])
    sums = []
    for column_index in range(column_count):
        colum_sum = 0
        for row_index in range(rows_count):
            colum_sum += matrix[row_index][column_index]
        sums.append(colum_sum)
    return sums


def print_result(values):
    [print(x) for x in values]


matrix = read_matrix()
result = column_sum(matrix)
print_result(result)
