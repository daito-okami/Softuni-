n = int(input())
diagonals = [input().split(", ") for line in range(n)]

first_d = []
second_d = []
col = n-1

for index in range(n):
    first_d.append(diagonals[index][index])
    second_d.append(diagonals[index][col])
    col -= 1


print(f"First diagonal: {', '.join(first_d)}. Sum: {sum(int(x) for x in first_d)}")
print(f"Second diagonal: {', '.join(second_d)}. Sum: {sum([int(x) for x in second_d])}")
