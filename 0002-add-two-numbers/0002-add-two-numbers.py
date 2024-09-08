# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            res = d1 + d2

            if carry == 1: 
                res += 1
                carry = 0
    
            if res > 9:
                curr.next = ListNode(res%10)
                carry = 1
            else:
                curr.next = ListNode(res)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return dummy.next
        
        
        # dummy = ListNode()
        # curr = dummy
        

        # def recur(ptr1, ptr2, carry):
        #     nonlocal curr
        #     if not ptr1 or not ptr2:
        #         pass

        #     num1 = ptr1.val if ptr1 else None
        #     num2 = ptr2.val if ptr2 else None

        #     value = (ptr2.val + ptr1.val + carry) % 10
        #     carry = 1 if (ptr1.val + ptr2.val + carry) > 9 else 0

        #     # Set the val
            
        #     curr.next = ListNode(value)

        #     curr = curr.next

        #     if ptr1:
        #         ptr1 = ptr1.next
        #     if ptr2:
        #         ptr2 = ptr2.next
        #     recur(ptr1, ptr2, carry)
        # recur(l1, l2, 0)

        # return dummy



        