class Solution(object):
    def makeFancyString(self, s):
        res = []
        res.append(s[0:2])
        for i in range(2,len(s)):
            if s[i] == s[i-1] and s[i] == s[i-2]:
                continue
            else:
                res.append(s[i])
        return "".join(res)
        
        