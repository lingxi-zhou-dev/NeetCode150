# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_list = []
        q_list = []
        self.helper(p, p_list)
        self.helper(q, q_list)
        print(p_list)
        print(q_list)
        if p_list != q_list:
            return False
        return True



    def helper(self, node, tree_list) -> list:
        if node is None:
            tree_list.append(1000)
            return None

        self.helper(node.left, tree_list)
        self.helper(node.right, tree_list)

        tree_list.append(node.val)

        return tree_list