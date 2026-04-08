# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# preorder tells you what node to create next
# inorder tells you where that node belongs (left vs right)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # build inorder index map
        self.inorder_map = {}
        for i, val in enumerate(inorder):
            self.inorder_map[val] = i

        # setup preorder index pointer
        self.pre_idx = 0

        return self.helper(preorder, inorder, 0, len(inorder)-1)
        
    def helper(self, preorder, inorder, left_bound, right_bound):
        if left_bound > right_bound:
            return None

        curr_val = preorder[self.pre_idx]
        self.pre_idx += 1

        root = TreeNode(curr_val)

        # identify the root node (middle index) in the inorder
        i_mid_idx = self.inorder_map[curr_val]

        # left of this node should have range left to middle
        root.left = self.helper(preorder, inorder, left_bound, i_mid_idx - 1)
        # right of this node should have range middle to right
        root.right = self.helper(preorder, inorder, i_mid_idx + 1, right_bound)

        return root