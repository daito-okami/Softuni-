from collections import deque

q = deque()
command = input()

while command != "End":
    if command == "Paid":
        while q:
            print(q.popleft())
    else:
        q.append(command)

    command = input()

print(f"{len(q)} people remaining.")