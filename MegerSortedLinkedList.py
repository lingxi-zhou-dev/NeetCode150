# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 2 -> 4
        # 1 -> 3 -> 5

        # compare the first nodes from list A and list B
        # compare #A1 and #B1
        # node #A1 is smaller
        # put the node #A1 on the new list
        # move the pointer to the #2 node of list A
        # compare #A2 to #B1
        # put #B2 on the new list
        # ...
        # until list A or list B reach None
        # then append the rest of the longer list on the new list
        # return new list

        list3 = None

        if list1 is None and list2 is None:
            return list3
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        # add first node to list3
        if list1.val >= list2.val:
            list3 = ListNode(list2.val)
            list2 = list2.next
        else:
            list3 = ListNode(list1.val)
            list1 = list1.next
        
        # save first node of list3
        list3_head = list3
        
        # When there are nodes left for both lists, compare and add
        while list1 and list2:
            
            if list1.val >= list2.val:
                # add the next list3 value
                list3.next = ListNode(list2.val)
                # move to the next list3 node
                list3 = list3.next
                list2 = list2.next
            else:
                # add the next list3 value
                list3.next = ListNode(list1.val)
                # move to the next list 3 node
                list3 = list3.next
                list1 = list1.next
            
        # When there are only nodes left for one list, add the rest of the nodes
        while list1:
            list3.next = ListNode(list1.val)
            list1 = list1.next
            list3 = list3.next
        while list2:
            list3.next = ListNode(list2.val)
            list2 = list2.next
            list3 = list3.next
        return list3_head