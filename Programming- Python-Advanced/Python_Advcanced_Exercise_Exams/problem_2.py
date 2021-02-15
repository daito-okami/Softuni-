def create_matrix(n):
    m = [list(input()) for _ in range(n)]
    return m


def search_matrix(matr, search):
    for y, row in enumerate(matr):
        for x, char in enumerate(row):
            if char == search:
                return y, x


def move(dy, dx):
    global snake_pos, game_over, food_quantity
    y, x = snake_pos
    matrix[y][x] = '.'
    new_y = y + dy
    new_x = x + dx
    if new_y > (n-1) or new_y < 0 or new_x > (n-1) or new_x < 0:
        game_over = True
        return
    position = matrix[new_y][new_x]
    if position == "B":
        matrix[new_y][new_x] = "."
        new_y, new_x = search_matrix(matrix, "B")
    elif position == "*":
        food_quantity += 1
        if food_quantity == 10:
            game_over = True
    matrix[new_y][new_x] = "S"
    snake_pos = (new_y, new_x)


def print_matrix(m):
    print('\n'.join([''.join(row)for row in m]))


n = int(input())
matrix = create_matrix(n)

snake_pos = search_matrix(matrix, "S")
game_over = False
food_quantity = 0


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


if game_over and food_quantity < 10:
    print("Game over!")
else:
    print("You won! You fed the snake.")

print(f"Food eaten: {food_quantity}")
print_matrix(matrix)
