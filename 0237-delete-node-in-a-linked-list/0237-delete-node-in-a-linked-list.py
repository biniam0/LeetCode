# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        left, right = node, node.next
        left.val = right.val
        left.next = right.next
        right.next = None
        