def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


n = int(input())
lines = input_to_list(n)

parking_lot = set()
for line in lines:
    action, plate = line.split(", ")
    if action == "IN":
        parking_lot.add(plate)
    else:
        parking_lot.remove(plate)

if len(parking_lot) > 0:
    for car in parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")