def convert_iterable_to_abs(nums_list):
    result = list(map(abs, nums_list))
    return result


nums = map(float, input().split())
print(convert_iterable_to_abs(nums))