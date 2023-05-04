class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums); i=0;j=1
        for k in range(len(nums)-1):
            if nums[k] == nums[k+1]:
                nums[k] *= 2
                nums[k+1] = 0
        while j < n:
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1 ; j += 1
            elif nums[i] == 0 and nums[j] == 0:
                j += 1
            else:
                i += 1; j+= 1
        return nums