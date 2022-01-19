'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        ended = []
        
        while len(ended) < len(lists): #filler
            smallest = lists[0].val
            for j in range(len(lists)):
                if lists[j]:
                    if lists[j].val < smallest:
                        smallest = lists[j].val
                    lists[j] = lists[j].next
                    if not lists[j]:
                        ended.append(j)

            current.next = ListNode(smallest)
            current = current.next
        
        return head.next
            
