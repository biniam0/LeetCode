# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        l, r = dummy, dummy.next

        while r:
            if r.val == val:
                l.next = r.next
            else:
                l = l.next
            r = r.next
        
        return dummy.next
