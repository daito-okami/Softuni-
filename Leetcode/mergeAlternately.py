class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = []
        i = 0

        while i<len(word1) or i < len(word2):
            if i <len(word1):
                merged.append(word1[i])
            if i <len(word2):
                merged.append(word2[i])
            i += 1

        return ''.join(merged)


print(Solution.mergeTwoLists("zzz", [1,2,4],[1,3,4]))