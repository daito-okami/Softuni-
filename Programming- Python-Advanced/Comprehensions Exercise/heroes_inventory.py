def update_heroes(name, item, price, heroes):
    if not heroes[name].get(item):
        heroes[name].update({item: int(price)})
    return heroes


names = input().split(", ")
heroes = {name: {} for name in names}
data = input()
while data != "End":
    name, item, price = data.split("-")
    heroes = update_heroes(name, item, price, heroes)

    data = input()

print(*[f"{key} -> Items: {len(items)}, Cost: {sum(items.values())}" for key, items in heroes.items()], sep="\n")