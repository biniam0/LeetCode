class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for item in logs:
            if item not in {"../", "./"}:
                stack.append(item)
            elif stack and item == "../":
                stack.pop()
        return len(stack)