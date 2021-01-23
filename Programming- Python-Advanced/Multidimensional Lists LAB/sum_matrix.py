def read_matrix():
    rows_count, column_count = map(int, input().split(", "))
    matrix = []
    for row_index in range(rows_count):
        row = list(map(int, input().split(", ")))
        matrix.append(row)
    return matrix


matrix = read_matrix()

matrix_sum = 0

for r in range(len(matrix)):
    row = matrix[r]
    row_sum = 0
    for c in range(len(row)):
        row_sum += row[c]

    matrix_sum += row_sum

print(matrix_sum)
print(matrix)