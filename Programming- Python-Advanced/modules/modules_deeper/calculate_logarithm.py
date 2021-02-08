from math import log

x = int(input())
base = input()

if base == "natural":
    print(log(x))
else:
    print(log(x, int(base)))