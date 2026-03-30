# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque   

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque([root])   
        master = []             
        
        # don't stop until queue is empty
        # process one level at a time
        while len(queue) != 0:
            sub = []
            level_len = len(queue)
            # process all the nodes in the queue
            for num in range(level_len):
                curr_node = queue.popleft()
                node_value = curr_node.val
                sub.append(node_value)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            master.append(sub)

        return master