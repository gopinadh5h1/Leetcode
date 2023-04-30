# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        current = root
        stack = [] # initialize stack
        ans  = []
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                ans.append(current.val)
                #print(current.data, end=" ") # Python 3 printing
                current = current.right
            else:
                break
        return ans