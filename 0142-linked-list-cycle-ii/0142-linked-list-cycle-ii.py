# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique_nodes = set()

        while head:
            if head in unique_nodes:
                return head
            unique_nodes.add(head)
            head = head.next
        
        return None