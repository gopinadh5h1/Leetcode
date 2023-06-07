class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        x = 1 ; y = 2
        for i in range(2,n):
            z = x + y
            x = y
            y = z
        return z
        