from sys import maxsize
rows, cols = [int(el) for el in input().split()]


def init_matrix():
    matrix = []
    for _ in range(rows):
        elements = [int(el) for el in input().split()]
        matrix.append(elements)

    return matrix


matrix = init_matrix()
best_r_1 = []
best_r_2 = []
best_r_3 = []
sum_best = -maxsize

for r in range(rows-2):
    for c in range(cols-2):
        elem_1 = matrix[r][c]
        elem_2 = matrix[r][c + 1]
        elem_3 = matrix[r][c + 2]
        elem_4 = matrix[r + 1][c]
        elem_5 = matrix[r + 1][c + 1]
        elem_6 = matrix[r + 1][c + 2]
        elem_7 = matrix[r + 2][c]
        elem_8 = matrix[r + 2][c + 1]
        elem_9 = matrix[r + 2][c + 2]

        current_sum = elem_1 + elem_2 + elem_3 + elem_4 + elem_5 + elem_6 + elem_7 + elem_8 + elem_9
        if current_sum > sum_best:
            sum_best = current_sum
            best_r_1 = []
            best_r_2 = []
            best_r_3 = []
            best_r_1 += elem_1, elem_2, elem_3
            best_r_2 += elem_4, elem_5, elem_6
            best_r_3 += elem_7, elem_8, elem_9

print(f"Sum = {sum_best}")
print(" ".join(map(str, best_r_1)))
print(" ".join(map(str, best_r_2)))
print(" ".join(map(str, best_r_3)))



