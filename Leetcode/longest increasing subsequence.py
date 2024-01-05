class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        list_of_counter = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] >nums[j]:
                    list_of_counter[i] = max(list_of_counter[i], 1 + list_of_counter[j])


        return max(list_of_counter)


print(Solution.lengthOfLIS("zzz", [10,9,2,5,3,7,101,18]))