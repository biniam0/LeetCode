# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        s, f = head, head

        while f.next and f.next.next:
            s = s.next
            f = f.next.next

        stack = []
        s = s.next
        while s:
            stack.append(s.val)
            s = s.next


        l = head
        ans = float("-inf")
        while stack and l:
            ans = max(ans, l.val + stack.pop())
            l = l.next

        return ans
            
        