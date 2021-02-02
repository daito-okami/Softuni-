def print_sum_nums(nums):
    positive_sum = sum(filter(lambda x: x > 0, nums))
    negative_sum = sum(filter(lambda x: x < 0, nums))
    print(negative_sum, positive_sum, sep="\n")
    if positive_sum > abs(negative_sum):
        print(f"The positives are stronger than the negatives")
        return
    print(f"The negatives are stronger than the positives")


numbers = list(map(int, input().split()))
print_sum_nums(numbers)