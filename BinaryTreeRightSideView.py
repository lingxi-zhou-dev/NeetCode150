# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # do a level traversal and just return the last element of each sub list
        if root is None:
            return []
        queue = deque([root])
        result = []

        while len(queue) != 0:
            inner = []
            level_len = len(queue)
            for num in range(level_len):
                node = queue.popleft()
                inner.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(inner[-1])

        return result