Divisor = int(input())
Bound = int(input())
maximum = 0

for N in range(1, Bound + 1):
    if N % Divisor == 0:
        maximum = N

print(maximum)