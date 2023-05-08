class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hm = {} ; count = 0
        for i in range(len(nums)):
            if (nums[i] in hm):
                hm[nums[i]] += 1
            else:
                hm[nums[i]] = 1
        for i in range(len(nums)):
            if k - nums[i] == nums[i] and hm[nums[i]] > 1:
                count += 1
                hm[nums[i]] -= 2
            elif (k-nums[i] != nums[i]) and (k-nums[i] in hm) and hm[k-nums[i]] > 0 and hm[nums[i]] > 0:
                count += 1
                hm[nums[i]] -= 1
                hm[k-nums[i]] -= 1
        return count
                
        