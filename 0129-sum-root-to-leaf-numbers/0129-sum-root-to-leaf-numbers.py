class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node, d):
            if not node:
                return 0

            d = d*10 + node.val
            if not node.left and not node.right:
                return d
            return helper(node.left, d) + helper(node.right, d)
        return helper(root, 0)



