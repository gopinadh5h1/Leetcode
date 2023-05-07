class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        count = 1
        for i in range(1,len(nums)):
            if count == 0:
                index = i
            if nums[i] == nums[index]:
                count += 1
            else:
                count -= 1
        return nums[index]
        