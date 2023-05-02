class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0 ; j = len(height)-1 ; area = 0 ; ans = 0
        while(i<j):
            area = (j-i) * min(height[i],height[j])
            ans = max(ans, area)
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1 ; j-= 1
        return ans
        