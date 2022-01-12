'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 or not list2:
            return list1 or list2
        
        head = list1 if list1.val < list2.val else list2
        current_node = head
        
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                current_node.val = list1.val
                list1 = list1.next
            else:
                current_node.val = list2.val
                list2 = list2.next
            
            current_node.next = ListNode()
            current_node = current_node.next
        
        current_node.val = list1.val if list1 else list2.val
        current_node.next = list1.next if list1 else list2.next
        
        return head
