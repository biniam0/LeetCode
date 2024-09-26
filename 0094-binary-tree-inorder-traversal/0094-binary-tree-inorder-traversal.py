# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res


        
        # if not root: 
        #     return []

        # stack = []

        # def inorder(node):
        #     if node:
        #         inorder(node.left)
        #         stack.append(node.val)
        #         inorder(node.right)
        
        # inorder(root)

        # return stack