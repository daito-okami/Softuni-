class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        res = 1
        for i in range(1,len(arr)):
            if (arr[i] > res):
                res += 1
        return res


print(Solution.maximumElementAfterDecrementingAndRearranging("zzz", [209,209,209,209,209,209,209,209,209,209,209]))