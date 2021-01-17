box = list(map(int, input().split()))
capacity = int(input())

rack_counter = 1

current_capacity = capacity
while len(box) > 0:
    curr_cloth = box.pop()

    if curr_cloth <= current_capacity:
        current_capacity -= curr_cloth
    else:
        rack_counter += 1
        current_capacity = capacity
        current_capacity -= curr_cloth

print(rack_counter)