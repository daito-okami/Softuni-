def stock_availability(items, action, *special_items):
    import functools
    from collections import deque
    items = deque(items)
    special_items_list = []
    for item in special_items:
        special_items_list.append(str(item))

    if action == "delivery":
        for item in special_items:
            items.append(item)
    if action == "sell":
        if len(special_items) == 0:
            items.popleft()
        for every_item in special_items_list:
            if every_item.isdigit():
                res = functools.reduce(lambda sub, ele: sub * 10 + ele, special_items)
                for el in wrange(res):
                    items.popleft()
            else:
                for el in range(len(items)):
                    if every_item in items:
                        items.remove(every_item)
                    else:
                        break

    return list(items)

# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
