class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i= 0 ; j=0
        while j < len(nums):
            if nums[j] != val:
                if i != j:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                i += 1; j+= 1
            else:
                j += 1
                
        return i
                
        
            
                
        