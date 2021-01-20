def input_to_list(count):
    lines = set()
    for _ in range(count):
        lines.add(input())

    return lines


def print_input_out(thing):
    for i in thing:
        print(i)


n = int(input())
print_input_out(input_to_list(n))