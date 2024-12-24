class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        ptr = 0

        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[ptr]:
                stack.pop()
                ptr += 1

        if not stack:
            return True
        return False
