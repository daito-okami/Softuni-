def input_to_set(count):
    lines = set()
    for _ in range(count):
        lines.add(input())

    return lines


splitter = input().split()
n = int(splitter[0])
m = int(splitter[1])

n_set = input_to_set(n)
m_set = input_to_set(m)
for val1 in n_set:
    for val2 in m_set:
        if val1 == val2:
            print(val2)