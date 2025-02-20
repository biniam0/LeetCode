# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=-101, next=head)

        l, r = dummy, dummy.next

        while r:
            if l.val == r.val:
                l.next = r.next
            else:
                l = l.next
            r = r.next

        return dummy.next