def odd_sum(numbers):
    result = sum(filter(lambda x: x % 2 != 0, numbers))
    result = result * len(numbers)
    return result


def even_sum(numbers):
    result = sum(filter(lambda x: x % 2 == 0, numbers))
    result = result * len(numbers)
    return result


command = input()
nums = [int(el) for el in input().split()]

if command == "Odd":
    print(odd_sum(nums))
elif command == "Even":
    print(even_sum(nums))