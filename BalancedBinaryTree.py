# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxDiff = 0
        self.helper(root)
        if self.maxDiff > 0:
            return False
        else:
            return True

    def helper(self, root):
        if root == None:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)

        diff = abs(left - right)

        if diff > 1:
            self.maxDiff += 1
        
        return 1 + max(left, right)