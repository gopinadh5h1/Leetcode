class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = '' ; i = 0
        m = len(word1); n = len(word2)
        while i < m and i < n:
            ans += word1[i] + word2[i]
            i += 1 
        ans += word1[i:m] + word2[i:n]
        return ans
            