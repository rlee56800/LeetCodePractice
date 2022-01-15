'''
Given the head of a linked list, return the list after sorting it in ascending order
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        cur_node = head
        node_list = []
        while cur_node != None:
            node_list.append([cur_node.val, cur_node])
            cur_node = cur_node.next
        
        node_list = sorted(node_list, key=lambda x: x[0])
        
        for i in range(len(node_list) - 1):
            node_list[i][1].next = node_list[i+1][1]
        
        node_list[-1][1].next = None
        
        return node_list[0][1]
