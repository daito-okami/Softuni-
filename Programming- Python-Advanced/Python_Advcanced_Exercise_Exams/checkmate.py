KING_SYMBOL = "K"
QUEEN_SYMBOL = 'Q'
def read_input(rows):
    matrix = []
    for _ in range(rows):
        matrix.append([el for el in input().split()])

    return matrix


def find_king_position(board):
    for row_index in range(len(board)):
        if KING_SYMBOL in board[row_index]:
            column_index = board[row_index].index(KING_SYMBOL)
            return (row_index, column_index)


def in_range(value, max_value):
    return 0 <= value < max_value


def search_with_deltas(board, king, deltas):
    rows_count = len(board)
    columns_count = len(board[0])
    delta_row, delta_column = deltas
    row_index, column_index = king

    while in_range(row_index, rows_count) and in_range(column_index, columns_count):
        if board[row_index][column_index] == QUEEN_SYMBOL:
            return [row_index, column_index]
        row_index += delta_row
        column_index += delta_column


def get_capturing_queens(board, king):

    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, +1),
        (+1, +1),
        (+1, 0),
        (+1, -1)
    ]

    queens = [
        search_with_deltas(board, king, delta)
        for delta in deltas
    ]
    return [queen for queen in queens if queen]


def print_result(queens):
    if queens:
        for queen in queens:
            print(queen)
    else:
        print("The king is safe!")


board = read_input(8)
king = find_king_position(board)
queens = get_capturing_queens(board, king)
print_result(queens)




