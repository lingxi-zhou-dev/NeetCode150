# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# we need in order traversal
# from left bottom to top, then go to the right subtree

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        treelist = []
        self.inOrderTraversal(root, treelist)
        return treelist[k-1]

    def inOrderTraversal(self, root, treelist) -> list:
        if root is None:
            return 
        # go all the way to the left
        self.inOrderTraversal(root.left, treelist)

        # add the value
        treelist.append(root.val)

        # go all the way to the right
        self.inOrderTraversal(root.right, treelist)

        return treelist