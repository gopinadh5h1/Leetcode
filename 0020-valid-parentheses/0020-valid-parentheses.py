class Solution(object):
    def isValid(self, A):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        n = len(A)
        for i in range(n):
            if A[i] == '}':
                if not len(stack):
                    return False
                top = stack.pop()
                if top != '{':
                    return False
            elif A[i] == ']':
                if not len(stack):
                    return False
                
                top = stack.pop()
                if top != '[':
                    return False
            elif A[i] == ')':
                if not len(stack):
                    return False
                
                top = stack.pop()
                if top != '(':
                    return False
            else:
                stack.append(A[i])
        return False if len(stack) else True
        