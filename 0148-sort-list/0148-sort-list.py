# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy.next
        lists = []

        while curr:
            lists.append(curr.val)
            curr = curr.next
            
        lists = sorted(lists)
        for num in lists:
            head.val = num
            head = head.next

        return dummy.next