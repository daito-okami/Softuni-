result = [' '.join(lists_as_string.split()) for lists_as_string in input().split("|")[::-1]]
print(" ".join(result))