quantity = int(input())
days = int(input())
day = 0
budget = 0
spirit_counter = 0

for day in range(1, days + 1):

    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        budget += 2 * quantity
        spirit_counter += 5

    if day % 3 == 0:
        budget += 8 * quantity
        spirit_counter += 13

    if day % 5 == 0:
        budget += 15 * quantity
        spirit_counter += 17
        if day % 3 == 0:
            spirit_counter += 30

    if day % 10 == 0:
        spirit_counter -= 20
        budget += 23
        if day == days:
            spirit_counter -=30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit_counter}")
