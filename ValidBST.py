# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -1001, 1001)

    def helper(self, root, left_limit, right_limit) -> bool:
        # base case: empty subtree is valid
        if root is None:
            return True
        
        # check current node
        if not (left_limit < root.val < right_limit):
            return False
        
        # recurse and adjust range
        # if both left tree and right tree are True, then True
        # if one of the sub trees are False then false
        return (self.helper(root.left, left_limit, root.val) and self.helper(root.right, root.val, right_limit))