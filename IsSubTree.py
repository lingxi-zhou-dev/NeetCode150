# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_list = []
        sub_list = []
        self.helper(root, root_list)
        self.helper(subRoot, sub_list)
        print(root_list)
        print(sub_list)
        r = 0
        s = 0
        if str(sub_list) in str(root_list):
            return True
        return False
        
    def helper(self, node, tree_list) -> list:
        if node is None:
            tree_list.append(1000)
            return None

        self.helper(node.left, tree_list)
        self.helper(node.right, tree_list)

        tree_list.append(node.val)
        return tree_list

