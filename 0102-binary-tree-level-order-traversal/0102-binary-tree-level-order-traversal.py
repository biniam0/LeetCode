# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dic = defaultdict(list)

        def dfs(node, depth):
            self.dic[depth].append(node.val)

            if node.left:
                dfs(node.left, depth + 1)
            
            if node.right:
                dfs(node.right, depth + 1)

        if root:
            dfs(root, 0)

        return [self.dic[i] for i in sorted(self.dic.keys())]




        # if not root:
        #     return []
        # queue = deque([root])
        # ans = []

        # while queue:
        #     level_size = len(queue)
        #     level = []
        #     for _ in range(level_size):
        #         node = queue.popleft()
        #         ans.append(node.val)

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     ans.append(level)

        # return ans

        