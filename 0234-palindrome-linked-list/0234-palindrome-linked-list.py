# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Solution with T(n) and S(1)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

        # Solution with T(n) and S(n)
        # nums = []
        # while head:
        #     nums.append(head.val)
        #     head = head.next

        # l, r = 0, len(nums)-1

        # while l <= r:
        #     if nums[l] != nums[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True