rows, cols = [int(el) for el in input().split()]


def init_matrix():
    matrix = []
    for _ in range(rows):
        matrix.append(input().split())

    return matrix


def check_el_equal(row, col, matr):
    elem_1 = matr[row][col]
    elem_2 = matr[row][col+1]
    elem_3 = matr[row+1][col]
    elem_4 = matr[row+1][col+1]
    if elem_1 == elem_2 and elem_2 == elem_3 and elem_3 == elem_4:
        return True
    return False


matrix = init_matrix()
counter = 0


for row_index in range(rows-1):
    for col_index in range(cols-1):
        if check_el_equal(row_index, col_index, matrix):
            counter +=1

print(counter)
