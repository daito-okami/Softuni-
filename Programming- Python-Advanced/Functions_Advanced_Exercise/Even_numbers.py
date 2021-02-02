def filter_even(iters):
    return filter(lambda x: x % 2 == 0, iters)


numbers = map(int, input().split())
print(list(filter_even(numbers)))
