from collections import deque


def list_manipulator(list_object, operation, position, *args):
    copied_list = deque(list_object.copy())
    if operation == "add":
        if len(args) > 0:
            if position == "beginning":
                copied_list = deque(args) + copied_list
            else:
                copied_list += deque(args)
    elif operation == "remove":
        if 0 <= len(args) <= 1:
            n = args[0] if len(args) == 1 else 1
            for _ in range(n):
                if position == "beginning":
                    copied_list.popleft()
                else:
                    copied_list.pop()

    return list(copied_list)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
