class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        ans = set()
        for i in nums2:
            if i in nums1:
                ans.add(i)
        return list(ans)