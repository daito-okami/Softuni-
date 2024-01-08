from functools import reduce


class Solution(object):
    def singleNumber(self, nums):
        while nums:
            checked_numer = nums.pop()
            if checked_numer not in nums:
                return int(checked_numer)
            else:
                nums.remove(checked_numer)
    def singleNumber2(self, nums): #second answer
        return reduce(lambda x, y: x ^ y, nums)


