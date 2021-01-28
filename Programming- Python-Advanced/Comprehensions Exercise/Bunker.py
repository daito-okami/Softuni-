categories = {c: [] for c in input().split(", ")}
n = int(input())

count_of_items = 0
quality_item = 0
for _ in range(n):
    category, item_name, item_params = input().split(" -")
    categories[category].append(item_name)
    count_of_items += int(item_params.split(';')[0].split(':')[1])
    quality_item += int(item_params.split(';')[1].split(':')[1])

print(f"Count of items: {count_of_items}")
print(f"Average quality: {quality_item/ len(categories):.2f}")
[print(f"{key} ->{','.join(value)}") for key, value in categories.items()]