class Solution(object): #test
    def twoSum(self, A, B):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}
        for i in range(len(A)):
            y = B - A[i]
            if y in hm.keys():
                return [hm[y], i]
            else:
                hm[A[i]] = i