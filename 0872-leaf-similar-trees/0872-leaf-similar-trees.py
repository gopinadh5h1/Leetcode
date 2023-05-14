# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafNodes(self,root,leaves):
        if root.left == None and root.right == None:
            leaves.append(root.val)
        if root.left:
            self.leafNodes(root.left,leaves)
        if root.right:
            self.leafNodes(root.right,leaves)
        return self.ans
    def leafSimilar(self, root1, root2):
        self.ans = []
        left  = [] ; right = []
        self.leafNodes(root1,left)
        self.leafNodes(root2,right)
        return left == right
        
        