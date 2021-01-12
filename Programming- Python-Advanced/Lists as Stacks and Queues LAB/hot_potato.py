from collections import deque

players = input().split()
step = int(input())

q = deque(players)
counter = 0

while len(q) > 1:
    q.rotate(-step + 1)
    print(f"Removed {q.popleft()}")


print(f"Last is {q.popleft()}")