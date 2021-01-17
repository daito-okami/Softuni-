from collections import deque

food_quantity = int(input())
order_quantities = deque(input().split())
order_quantities_int = [int(el) for el in order_quantities]
print(max(order_quantities_int))
uncompleted_orders = 0

while order_quantities:
    if food_quantity >= int(order_quantities[0]):
        food_quantity -= int(order_quantities[0])
        order_quantities.popleft()
    else:
        uncompleted_orders = 1
        break
result = ''
if uncompleted_orders == 0:
    print("Orders complete")
else:
    for el in order_quantities:
        result += el + " "
    print(f"Orders left: {result}")