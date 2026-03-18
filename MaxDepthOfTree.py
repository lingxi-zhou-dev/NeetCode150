# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        node = root
        d = []
        # how to add every return into the d list?
        self.helper(node, count, d)
        print(d)
        return max(d)
    
    def helper(self, node, count, d):
        # stop when node is none, then add that count to list
        if node is None:
            d.append(count)
            return count
        
        # if node is not none then go left and right
        self.helper(node.left, count + 1, d)
        self.helper(node.right, count + 1, d)