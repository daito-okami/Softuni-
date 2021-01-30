def round_iter_elements(nums_list):
    result = [round(el) for el in nums_list]
    return result


nums = map(float, input().split())
print(round_iter_elements(nums))