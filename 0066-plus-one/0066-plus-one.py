class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n= len(digits)
        x = 0 ; ans = []
        for i in range(n):
            x = x*10 + digits[i]
        x += 1
        while x != 0:
            ans.append(x % 10)
            x //= 10
        return ans[::-1]
            
        