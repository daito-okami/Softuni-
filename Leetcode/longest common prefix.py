class Solution:
    def longestCommonPrefix(self, strs):

        prefix = strs[0]
        #We assume that the first list will be what is the longest common prefix and remove 1 character wtih each unmatch

        for i in strs:
            while not i.startswith(prefix):
                prefix = prefix[:-1]

        return prefix



print(Solution.longestCommonPrefix("zz", ["flower","flow","flight"]))
