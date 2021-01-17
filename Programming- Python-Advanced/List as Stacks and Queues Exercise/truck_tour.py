from collections import deque

n = int(input())

station = deque([])
is_valid = True


for _ in range(n):
    station.append(input())


for big_circle in range(n):
    tank = 0
    is_valid = True
    for small_circle in range(n):
        current_station = station[small_circle]
        petrol, distance = current_station.split()
        petrol = int(petrol)
        distance = int(distance)
        tank += petrol - distance
        if tank < 0:
            is_valid = False
            station.append(station.popleft())
            break

    if is_valid:
        print(big_circle)
        break