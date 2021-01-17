def push(stack, num):
    num = int(num)
    if 1 <= num <= 109:
        stack.append(num)
    return stack


def delete(stack):
    if stack:
        a = stack.pop()
    return stack


def max_num(stack):
    print(max(stack))
    return stack


def min_num(stack):
    print(min(stack))
    return stack


s = []
result = []

n = int(input())

if 1 <= n <= 105:
    for i in range(n):
        command = input()
        if command.startswith("1"):
            command, x = command.split()
            s = push(s, x)
        elif command.startswith("2"):
            s = delete(s)
        elif command.startswith("3"):
            s = max_num(s)
        elif command.startswith("4"):
            s = min_num(s)

while s:
    result.append(s.pop())

string_result = [str(el) for el in result]
print(", ".join(string_result))