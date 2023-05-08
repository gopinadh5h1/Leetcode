class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        a = " ".join(s.split()[::-1])
        return a
        