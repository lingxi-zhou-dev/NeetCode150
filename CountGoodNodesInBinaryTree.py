# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# we have to use DFS here
# For each node, we get the max_val so far
# if node.val >= max_val
# good_count += 1

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_count = 0
        max_val = root.val
        self.dfs(root, max_val)
        return self.good_count

    def dfs(self, root, max_val):
        if root is None:
            return

        curr_val = root.val
        # update max_val at this point
        # if the curr val is bigger than previous val -> then good_count + 1
        if max_val <= curr_val:
            max_val = curr_val
            self.good_count += 1

        self.dfs(root.left, max_val)
        self.dfs(root.right, max_val)