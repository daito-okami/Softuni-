def periodic_table(n):
    table = set()
    for _ in range(n):
        elements = input().split()
        for el in elements:
            table.add(el)

    return table


n = int(input())
result = periodic_table(n)
for i in result:
    print(i)
