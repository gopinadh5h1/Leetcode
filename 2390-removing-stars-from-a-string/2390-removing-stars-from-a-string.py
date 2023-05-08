class Solution(object):
    def removeStars(self, s):
        stack= []
        for i in s:
            if i == '*':
                stack.pop(-1)
            else:
                stack.append(i)
        return ''.join(stack)
        