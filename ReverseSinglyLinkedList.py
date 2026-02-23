# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 -> 1 -> 2 -> 3 
    #          next         
    #     p1 -> p2   
        if not head:
            return None

        prev = None
        curr = head
        
        while curr != None:
            # save the next node
            Next = curr.next
            # reverse arrow
            curr.next = prev
            # after the arrow is reversed the previous linked relationship is destroyed
            prev = curr
            curr = Next
            
        return prev