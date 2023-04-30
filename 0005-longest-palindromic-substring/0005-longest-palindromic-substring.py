class Solution(object):
    def palindrome(self, A, s1, s2):
        while ((s1>=0 and s2< len(A) ) and (A[s1] == A[s2])):
            s1 -= 1
            s2 += 1
        return A[s1+1:s2]
    def longestPalindrome(self, A):
        """
        :type s: str
        :rtype: str
        """
        n = len(A)
        ans = A[0]
        for i in range(n):
            temp = self.palindrome(A,i,i)
            if len(temp) > len(ans):
                ans = temp
            #ans = max(ans, palindrome("A",A,i,i))
        for i in range(n-1):
            temp = self.palindrome(A,i,(i+1))
            if len(temp) > len(ans):
                ans = temp
        return ans

        