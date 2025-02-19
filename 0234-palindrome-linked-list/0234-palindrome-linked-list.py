# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        right = head
        left = head
        stack = []
        while right and right.next:
            stack.append(left.val)
            right = right.next.next
            left = left.next

        if right:
            left = left.next

        while stack and left:
            if stack.pop() != left.val:
                return False
            left = left.next

        return True