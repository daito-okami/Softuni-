rows = int(input())
matrix = [input().split(", ") for _ in range(rows)]

print([int(x) for row in matrix for x in row])