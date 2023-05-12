class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = '' ; i = 0; j = 0
        m = len(word1); n = len(word2)
        while i < m and j < n:
            ans += word1[i] + word2[j]
            i += 1 ; j += 1
        ans += word1[i:m] + word2[j:n]
        return ans
            