text = input().split(", ")
result = [f"{name} -> {len(name)}" for name in text]
print(', '.join(result))