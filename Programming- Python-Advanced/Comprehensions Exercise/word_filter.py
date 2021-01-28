text = input().split()

result = "\n".join([x for x in text if len(x) % 2 == 0])
print(result)