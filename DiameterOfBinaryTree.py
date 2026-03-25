# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from left most node to the right most
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # End node doesn't have left or right nodes
        node = root
        count = 0
        self.max_diameter = 0
        self.find_diameter(node)
        return self.max_diameter
        

    def find_diameter(self, node) -> int:
        if node == None:
            return 0

        # getting to the bottom of each tree
        # when getting to the bottom the count will be 0
        # then return to the previous node with 0 height
        left_height = self.find_diameter(node.left)
        right_height = self.find_diameter(node.right)

        # curr_diameter is temporary just to update the max diameter
        curr_diameter = left_height + right_height

        self.max_diameter = max(curr_diameter, self.max_diameter)

        # return to the function caller (could be line 25, 26) with the latest height
        return 1 + max(left_height, right_height)