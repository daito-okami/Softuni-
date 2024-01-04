class Solution(object):                   # First solution
    def findContentChildren(self, g, s):
        satisfied_children = 0
        size_len = len(s)

        g.sort()
        s.sort()
        while g and s:
            current_child = g[-1]
            current_size = s[-1]

            if current_child in s:
                s.remove(current_child)
                satisfied_children += 1
            elif current_child <= s[-1]:
                s.remove(current_size)
                satisfied_children += 1
            g.pop()


        return satisfied_children



class Solution(object): # Second solution
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        satisfied_children = 0
        current_child = 0
        current_cookie = 0
        while current_child < len(g) and current_cookie < len(s):
            if s[current_cookie] >= g[current_child]:
                satisfied_children += 1
                current_child += 1
            current_cookie += 1
        return satisfied_children


# Greed factor(g)= the minium amount a child will be content with
# Size factor(s)= the size of the cookie
# if size=>greed, the child will be satisfied with the cookie
