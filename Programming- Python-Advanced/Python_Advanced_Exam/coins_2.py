from math import floor


def create_matrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append([el for el in input().split()])
    return matrix


def search_matrix(matr, search):
    for y, row in enumerate(matr):
        for x, char in enumerate(row):
            if char == search:
                return y, x


def move(dy, dx):
    global player, game_over, coins, matrix, moves
    y, x = player
    matrix[y][x] = '0'
    new_y = y + dy
    new_x = x + dx
    if new_y > (n-1) or new_y < 0 or new_x > (n-1) or new_x < 0:
        coins = floor(coins / 2)
        game_over = True
        return
    player = new_y, new_x
    if matrix[new_y][new_x] == "X":
        game_over = True
        coins = floor(coins / 2)
        return
    else:
        coins += float(matrix[new_y][new_x])
        if coins >= 100:
            game_over = True

    matrix[new_y][new_x] = "P"
    moves.append([new_y, new_x])



game_over = False
n = int(input())
matrix = create_matrix(n)
player = search_matrix(matrix, "P")
coins = 0
moves = []

while not game_over:
    command = input()
    if command == "up":
        move(-1, 0)
    elif command == "down":
        move(+1, 0)
    elif command == "left":
        move(0, -1)
    elif command == "right":
        move(0, 1)

if coins >= 100:
    print(f"You won! You've collected {coins:.0f} coins.")
else:
    print(f"Game over! You've collected {coins:.0f} coins.")

print("Your path:")
for el in moves:
    print(el)
