class Solution(object):
    def bsearch(self,nums,target,l,r):
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif l > r:
            return l
        elif target < nums[mid]:
            return self.bsearch(nums,target,l,mid-1)
        else:
            return self.bsearch(nums,target,mid+1,r)
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.bsearch(nums,target,0,len(nums)-1)
        
        