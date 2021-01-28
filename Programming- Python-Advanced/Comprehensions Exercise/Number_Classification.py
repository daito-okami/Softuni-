numbers = [int(x) for x in input().split(", ")]
positive = []
negative = []
even = []
odd = []

for i in numbers:
    if i >= 0:
        positive.append(i)
    if i < 0:
        negative.append(i)
    if i % 2 == 0:
        even.append(i)
    if i % 2 != 0:
        odd.append(i)

print(f"Positive: {', '.join([str(x) for x in positive])}")
print(f"Negative: {', '.join([str(x) for x in negative])}")
print(f"Even: {', '.join([str(x) for x in even])}")
print(f"Odd: {', '.join([str(x) for x in odd])}")
