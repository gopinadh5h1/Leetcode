class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0; j=1; m = nums[0]
        while(j<len(nums)):
            if nums[j] > m:
                nums[i+1] = nums[j]
                i += 1; j += 1
                m = nums[i]
            else:
                j += 1
        return i+1
        